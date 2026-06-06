"""
06_shorts.py -- The Shorts Factory
Takes finished final_render.mp4 + data.json -> extracts vertical YouTube Shorts.
Uses Gemini to pick story-driven segments that work as standalone mini-narratives.
Center-crops 16:9 -> 9:16 via ffmpeg. Burns subtitles via Whisper + custom font.
Uploads each Short to YouTube.

Usage:
    python 06_shorts.py                  # generate + upload
    python 06_shorts.py --dry-run        # generate only, skip upload
    python 06_shorts.py --no-upload      # same as --dry-run
"""
import json
import math
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from google import genai

from config import (
    DATA_JSON,
    FINAL_RENDER,
    GEMINI_API_KEY,
    SHORT_MAX_DURATION,
    SHORT_MIN_DURATION,
    SHORT_TARGET_DURATION,
    SHORTS_DIR,
)

# ── Paths ──────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parent / "resources"
FONT_PATH = RESOURCES_DIR / "KOMIKAX_.ttf"

# ── Retry constants ────────────────────────────────────────────
MAX_SERVER_RETRIES = 4
SERVER_RETRY_BASE_DELAY = 5
MAX_PARSE_RETRIES = 2


# ── JSON Parsing (robust) ─────────────────────────────────────

def _extract_json_brace(raw: str) -> dict:
    """Extract JSON via brace-matching (fallback when direct parse fails)."""
    for open_ch, close_ch in [("{", "}"), ("[", "]")]:
        start = raw.find(open_ch)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(raw)):
            if raw[i] == open_ch:
                depth += 1
            elif raw[i] == close_ch:
                depth -= 1
                if depth == 0:
                    extracted = raw[start:i + 1]
                    fixed = re.sub(r",\s*([}\]])", r"\1", extracted)
                    return json.loads(fixed)
    raise ValueError("No valid JSON found in response")


def _call_gemini_json(client, prompt: str, system: str, label: str = "") -> dict:
    """Call Gemini -> parse JSON. Retries on server errors + parse errors."""
    last_error = None
    for parse_attempt in range(MAX_PARSE_RETRIES + 1):
        for server_attempt in range(MAX_SERVER_RETRIES + 1):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        system_instruction=system,
                        response_mime_type="application/json",
                        max_output_tokens=16384,
                    ),
                )
                raw = response.text.strip()
                if raw.startswith("```"):
                    raw = re.sub(r"^```(?:json)?\s*", "", raw)
                    raw = re.sub(r"\s*```\s*$", "", raw)
                raw = re.sub(r",\s*([}\]])", r"\1", raw)
                try:
                    return json.loads(raw)
                except json.JSONDecodeError:
                    return _extract_json_brace(raw)
            except (json.JSONDecodeError, ValueError) as e:
                last_error = e
                print(f"[SHORTS]   [!] Parse error ({label}, try {parse_attempt + 1}): {e}")
                break
            except Exception as e:
                status = getattr(e, "status_code", 0) or 0
                is_retryable = status in (429, 500, 503) or "503" in str(e) or "UNAVAILABLE" in str(e)
                if is_retryable and server_attempt < MAX_SERVER_RETRIES:
                    delay = SERVER_RETRY_BASE_DELAY * (2 ** server_attempt)
                    print(f"[SHORTS]   [!] Server error ({label}, attempt {server_attempt + 1}/{MAX_SERVER_RETRIES + 1}), retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    raise

    raise RuntimeError(f"Failed to parse Gemini response for {label} after {MAX_PARSE_RETRIES + 1} tries: {last_error}")


# ── Phase 1: Story-Driven Segment Selection ────────────────────

def _build_block_timeline(data: dict) -> list[dict]:
    """Build timeline with cumulative timestamps from block durations."""
    timeline = []
    cursor = 0.0
    for block in data.get("blocks", []):
        dur = block.get("voice_duration_sec", 15.0)
        timeline.append({
            "block_id": block["block_id"],
            "start_sec": round(cursor, 3),
            "end_sec": round(cursor + dur, 3),
            "duration": round(dur, 3),
            "voiceover": block["voiceover"],
        })
        cursor += dur
    return timeline


def _select_segments(data: dict, timeline: list[dict]) -> list[dict]:
    """Use Gemini to pick story-driven segments that work as standalone Shorts."""
    client = genai.Client(api_key=GEMINI_API_KEY)

    total_duration = timeline[-1]["end_sec"] if timeline else 0

    # Build block info
    block_summaries = []
    for t in timeline:
        block_summaries.append(
            f"Block {t['block_id']} [{t['start_sec']:.1f}s-{t['end_sec']:.1f}s] "
            f"({t['duration']:.1f}s): {t['voiceover']}"
        )
    blocks_text = "\n".join(block_summaries)

    system = (
        "You are an expert YouTube Shorts editor specializing in science documentaries. "
        "Your job is to find segments from a long documentary that tell a COMPLETE MINI-STORY "
        "on their own. Each Short must hook the viewer, deliver an insight, and feel satisfying "
        "-- not like a random clip cut from a longer video. Think of each Short as a "
        "standalone 30-second documentary episode."
    )

    prompt = f"""Analyze this documentary and find segments that tell COMPLETE MINI-STORIES.

CRITICAL RULES:
- Each Short MUST tell a self-contained story with: HOOK (curiosity trigger) -> INSIGHT (the interesting fact/revelation) -> PAYOFF (satisfying conclusion or mind-blowing implication)
- Target duration: exactly ~{SHORT_TARGET_DURATION} seconds per Short (1 block = ~25-35s, perfect for one Short)
- Each segment = exactly 1 block (single block gives ~30s, ideal for Shorts)
- Segments MUST NOT overlap
- SKIP blocks that are purely transitional, introductory setup, or "next time" outros
- SKIP blocks that reference "previous" or "next" sections (they don't work standalone)
- Only pick blocks where the voiceover tells a COMPLETE thought -- a viewer seeing ONLY this Short should learn something fascinating and feel satisfied
- Pick as many qualifying blocks as possible, but QUALITY over QUANTITY -- every Short must be worth watching on its own

WHAT MAKES A GOOD SHORT:
- A mind-blowing fact ("Dark matter makes up 27% of the universe but we can't see it")
- A vivid scenario ("Rogue planets drift alone through interstellar space, unattached to any star")
- A compelling mystery ("Why do galaxies spin faster than they should?")
- An awe-inspiring scale comparison ("Roman's camera captures 100x more sky than Hubble")

WHAT MAKES A BAD SHORT (DO NOT PICK):
- Generic transitions ("Let's now explore...")
- Blocks that start with "And so..." or "As we've seen..."
- Blocks that only make sense in context of surrounding blocks
- Pure historical summary without a hook

DOCUMENTARY TITLE: {data.get('title', '')}

BLOCK TIMELINE (full voiceover text for each block):
{blocks_text}

For each selected Short, generate:
- A catchy, curiosity-driven title (max 80 chars)
- A 2-sentence description with hashtags
- 5-8 relevant tags

Output as JSON:
{{
  "shorts": [
    {{
      "block_id": <int>,
      "start_sec": <float>,
      "end_sec": <float>,
      "title": "<catchy title>",
      "description": "<2 sentences with hashtags>",
      "tags": ["tag1", "tag2", ...],
      "story_hook": "<1 sentence explaining why this works as a standalone Short>"
    }}
  ]
}}"""

    print(f"[SHORTS] Asking Gemini to find story-driven segments...")
    result = _call_gemini_json(client, prompt, system, "segment_selection")

    segments = result.get("shorts", [])
    print(f"[SHORTS] Gemini found {len(segments)} story-worthy segments")

    # Validate
    valid = []
    for seg in segments:
        dur = seg.get("end_sec", 0) - seg.get("start_sec", 0)
        if dur < SHORT_MIN_DURATION:
            print(f"[SHORTS]   [!] Skip (too short {dur:.1f}s): {seg.get('title', '?')[:50]}")
            continue
        if dur > SHORT_MAX_DURATION:
            seg["end_sec"] = seg["start_sec"] + SHORT_MAX_DURATION
            dur = SHORT_MAX_DURATION
        seg["duration"] = round(dur, 1)
        hook = seg.get("story_hook", "")
        print(f"[SHORTS]   [OK] Block {seg.get('block_id', '?')}: {seg.get('title', '?')[:60]}")
        if hook:
            print(f"[SHORTS]        Reason: {hook[:80]}")
        valid.append(seg)

    print(f"[SHORTS] {len(valid)} valid story-driven segments")
    return valid


# ── Phase 2: Extract + Crop ───────────────────────────────────

def _extract_and_crop_short(source: Path, start: float, end: float, output: Path) -> bool:
    """Extract segment + center-crop 16:9 -> 9:16 in one ffmpeg pass."""
    duration = end - start
    # Center crop 608x1080 from 1920x1080, then scale to 1080x1920
    vf = "crop=608:1080:656:0,scale=1080:1920:flags=lanczos"

    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-ss", f"{start:.3f}",
                "-i", str(source),
                "-t", f"{duration:.3f}",
                "-vf", vf,
                "-c:v", "libx264",
                "-preset", "medium",
                "-crf", "20",
                "-c:a", "aac",
                "-b:a", "128k",
                "-movflags", "+faststart",
                str(output),
            ],
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"[SHORTS]   [X] ffmpeg extract failed: {e.stderr.decode()[:300]}")
        return False


# ── Phase 3: Whisper Subtitles ─────────────────────────────────

def _transcribe_audio(video_path: Path) -> list[dict]:
    """Transcribe video audio using Whisper -> word-level timestamps."""
    import whisper

    print(f"[SHORTS]     Transcribing with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(
        str(video_path),
        word_timestamps=True,
        language="en",
    )

    # Extract word-level segments
    words = []
    for segment in result.get("segments", []):
        for word_info in segment.get("words", []):
            words.append({
                "word": word_info["word"].strip(),
                "start": word_info["start"],
                "end": word_info["end"],
            })
    return words


def _words_to_subtitle_groups(words: list[dict], max_words: int = 4) -> list[dict]:
    """Group words into subtitle chunks (max N words per line)."""
    groups = []
    i = 0
    while i < len(words):
        chunk_words = words[i:i + max_words]
        text = " ".join(w["word"] for w in chunk_words)
        start = chunk_words[0]["start"]
        end = chunk_words[-1]["end"]
        groups.append({"text": text.upper(), "start": start, "end": end})
        i += max_words
    return groups


def _generate_ass_subtitles(groups: list[dict], output_path: Path, font_name: str = "Komika Axis"):
    """Generate ASS subtitle file with styled text for ffmpeg burning."""
    # ASS header with custom font styling
    header = f"""[Script Info]
Title: Shorts Subtitles
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,{font_name},62,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,180,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    events = []
    for g in groups:
        start_ts = _seconds_to_ass_time(g["start"])
        end_ts = _seconds_to_ass_time(g["end"])
        # Clean text for ASS format
        text = g["text"].replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
        events.append(f"Dialogue: 0,{start_ts},{end_ts},Default,,0,0,0,,{text}")

    content = header + "\n".join(events) + "\n"
    output_path.write_text(content, encoding="utf-8")
    return output_path


def _seconds_to_ass_time(seconds: float) -> str:
    """Convert seconds to ASS time format: H:MM:SS.CC"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int((seconds % 1) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def _burn_subtitles(video_path: Path, ass_path: Path, output_path: Path) -> bool:
    """Burn ASS subtitles into video using ffmpeg with custom font."""
    # Build font directory for ffmpeg
    fonts_dir = str(RESOURCES_DIR).replace("\\", "/").replace(":", "\\\\:")

    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(video_path),
                "-vf", f"ass={str(ass_path).replace(chr(92), '/').replace(':', chr(92)+':')}:fontsdir={fonts_dir}",
                "-c:v", "libx264",
                "-preset", "medium",
                "-crf", "20",
                "-c:a", "copy",
                "-movflags", "+faststart",
                str(output_path),
            ],
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"[SHORTS]   [X] Subtitle burn failed: {e.stderr.decode()[:400]}")
        return False


def _add_subtitles_to_short(video_path: Path) -> bool:
    """Full subtitle pipeline: transcribe -> generate ASS -> burn into video."""
    ass_path = video_path.with_suffix(".ass")
    temp_path = video_path.with_name(video_path.stem + "_nosub.mp4")

    # Transcribe
    words = _transcribe_audio(video_path)
    if not words:
        print(f"[SHORTS]     [!] No words detected, skipping subtitles")
        return True  # not a failure, just no speech

    # Group words into subtitle chunks
    groups = _words_to_subtitle_groups(words, max_words=3)
    print(f"[SHORTS]     {len(words)} words -> {len(groups)} subtitle groups")

    # Generate ASS file
    _generate_ass_subtitles(groups, ass_path)

    # Rename original -> temp, burn subs -> original path
    video_path.rename(temp_path)

    ok = _burn_subtitles(temp_path, ass_path, video_path)
    if ok:
        temp_path.unlink(missing_ok=True)
        ass_path.unlink(missing_ok=True)
        print(f"[SHORTS]     [OK] Subtitles burned")
    else:
        # Restore original
        if temp_path.exists():
            temp_path.rename(video_path)
        print(f"[SHORTS]     [X] Subtitle burn failed, using original")

    return ok


# ── Phase 4: Upload ────────────────────────────────────────────

def _upload_short(youtube, short_path: Path, meta: dict, full_video_id: str = None) -> str:
    """Upload a single Short to YouTube."""
    from googleapiclient.http import MediaFileUpload

    title = meta["title"]
    if not any(tag in title.lower() for tag in ["#short", "#shorts"]):
        title = title[:77] + " #Shorts" if len(title) > 77 else title + " #Shorts"

    desc = meta.get("description", "")
    if full_video_id:
        desc += f"\n\nFull documentary: https://youtube.com/watch?v={full_video_id}"
    desc += "\n\nThis video contains AI-generated synthetic visuals."

    body = {
        "snippet": {
            "title": title[:100],
            "description": desc,
            "tags": meta.get("tags", []),
            "categoryId": "28",
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        str(short_path),
        mimetype="video/mp4",
        resumable=True,
        chunksize=5 * 1024 * 1024,
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"[SHORTS]     {pct}% uploaded")

    return response["id"]


# ── Orchestrator ───────────────────────────────────────────────

def generate_shorts(full_video_id: str = None, upload: bool = True) -> list[dict]:
    """Main pipeline: select story segments -> extract -> subtitle -> upload."""
    if not FINAL_RENDER.exists():
        raise FileNotFoundError(f"No video found at {FINAL_RENDER}")
    if not DATA_JSON.exists():
        raise FileNotFoundError(f"No data.json found at {DATA_JSON}")

    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    SHORTS_DIR.mkdir(parents=True, exist_ok=True)
    for old in SHORTS_DIR.glob("short_*.mp4"):
        old.unlink()

    print("=" * 60)
    print("  SHORTS FACTORY -- Generating YouTube Shorts")
    print("=" * 60)

    # ── Phase 1: Select story segments ──
    print("\n[SHORTS] Phase 1: Finding story-driven segments...")
    timeline = _build_block_timeline(data)
    total_video_dur = timeline[-1]["end_sec"] if timeline else 0
    print(f"[SHORTS] Video duration: {total_video_dur:.1f}s ({total_video_dur/60:.1f}min)")

    segments = _select_segments(data, timeline)
    if not segments:
        print("[SHORTS] [X] No valid segments found. Aborting.")
        return []

    # ── Phase 2: Extract + crop ──
    print(f"\n[SHORTS] Phase 2: Extracting {len(segments)} shorts...")
    extracted = []
    for i, seg in enumerate(segments, 1):
        short_path = SHORTS_DIR / f"short_{i:02d}.mp4"
        print(f"[SHORTS]   [{i}/{len(segments)}] {seg['title'][:50]}...")
        print(f"[SHORTS]     Time: {seg['start_sec']:.1f}s -> {seg['end_sec']:.1f}s ({seg['duration']}s)")

        ok = _extract_and_crop_short(
            FINAL_RENDER, seg["start_sec"], seg["end_sec"], short_path,
        )
        if ok:
            seg["file"] = short_path
            extracted.append(seg)
            print(f"[SHORTS]     [OK] Extracted -> {short_path.name}")
        else:
            print(f"[SHORTS]     [X] Extraction failed, skipping")

    if not extracted:
        print("[SHORTS] [X] No shorts extracted. Aborting.")
        return []

    print(f"\n[SHORTS] [OK] {len(extracted)}/{len(segments)} shorts extracted")

    # ── Phase 3: Add subtitles via Whisper ──
    if FONT_PATH.exists():
        print(f"\n[SHORTS] Phase 3: Adding subtitles (Whisper + {FONT_PATH.name})...")
        for i, seg in enumerate(extracted, 1):
            print(f"[SHORTS]   [{i}/{len(extracted)}] Subtitling: {seg['file'].name}")
            _add_subtitles_to_short(seg["file"])
    else:
        print(f"\n[SHORTS] [!] Font not found at {FONT_PATH}, skipping subtitles")

    # ── Phase 4: Upload ──
    if not upload:
        print("\n[SHORTS] >> Upload skipped (dry-run mode)")
        _save_shorts_metadata(extracted)
        return extracted

    print(f"\n[SHORTS] Phase 4: Uploading {len(extracted)} shorts to YouTube...")
    import importlib
    pub = importlib.import_module("05_publisher")
    youtube = pub._get_authenticated_service()

    results = []
    for i, seg in enumerate(extracted, 1):
        print(f"[SHORTS]   [{i}/{len(extracted)}] Uploading: {seg['title'][:50]}...")
        try:
            video_id = _upload_short(youtube, seg["file"], seg, full_video_id)
            seg["youtube_id"] = video_id
            seg["youtube_url"] = f"https://youtube.com/shorts/{video_id}"
            print(f"[SHORTS]     [OK] Uploaded -> {seg['youtube_url']}")
            results.append(seg)
        except Exception as e:
            print(f"[SHORTS]     [X] Upload failed: {e}")
            seg["youtube_id"] = None
            results.append(seg)

    _save_shorts_metadata(results)

    # Summary
    uploaded_count = sum(1 for r in results if r.get("youtube_id"))
    print(f"\n{'=' * 60}")
    print("  SHORTS FACTORY -- Complete")
    print(f"  {uploaded_count}/{len(results)} shorts uploaded successfully")
    print(f"  Files: {SHORTS_DIR}")
    for r in results:
        status = f"[OK] {r['youtube_url']}" if r.get("youtube_id") else "[X] failed"
        print(f"     {r['title'][:60]} -> {status}")
    print("  [!] All shorts uploaded as PRIVATE -- review in YouTube Studio")
    print("=" * 60)

    return results


def _save_shorts_metadata(shorts: list[dict]):
    """Save shorts metadata to JSON for reference."""
    meta_path = SHORTS_DIR / "shorts_metadata.json"
    serializable = []
    for s in shorts:
        entry = {k: v for k, v in s.items() if k != "file"}
        if "file" in s:
            entry["file"] = str(s["file"])
        serializable.append(entry)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
    print(f"[SHORTS] Metadata saved -> {meta_path}")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv or "--no-upload" in sys.argv
    vid_id = None
    for arg in sys.argv[1:]:
        if arg.startswith("--video-id="):
            vid_id = arg.split("=", 1)[1]
    generate_shorts(full_video_id=vid_id, upload=not dry_run)
