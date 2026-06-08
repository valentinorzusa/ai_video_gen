"""
03_vision.py -- The Scout/Generator (ComfyUI IA2V + Pexels Edition)
====================================================================
Reads data.json. For each block decides the clip source:
  • ~60% → ComfyUI AI generation (Gemini image → LTXV video)
  • ~40% → Pexels stock footage

ComfyUI path (per block):
  1. Generate a base image via Gemini
  2. Upload image + block audio to ComfyUI
  3. Inject prompt, image filename, audio filename into workflow
  4. Poll ComfyUI for the resulting video clip
  5. Trim to exact voice duration (NO LOOPING — concatenate new clips if needed)

Pexels path (per block):
  1. Search Pexels Videos API with block's pexels_query
  2. Download best-matching landscape clip >= needed duration
  3. If one clip too short, fetch more and concatenate (NO LOOPING)
  4. Trim concat to exact voice duration
"""
import json
import subprocess
import sys
import time
import uuid
from pathlib import Path

# Force UTF-8 output on Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8")

import requests
from google import genai

from config import (
    BASE_DIR,
    CLIPS_DIR,
    TEMP_DIR,
    DATA_JSON,
    COMFYUI_URL,
    COMFYUI_WORKFLOW,
    COMFYUI_PROMPT_NODE,
    COMFYUI_TIMEOUT,
    GEMINI_API_KEY,
    PEXELS_API_KEY,
)

# ---------------------------------------------------------------------------
# Pexels mix ratio — every 5 blocks, the last 2 use Pexels (40%)
# Block indices within each group:  0,1,2 → AI   3,4 → Pexels
# ---------------------------------------------------------------------------
_PEXELS_SLOT_MOD = 5       # group size
_PEXELS_SLOT_FROM = 3      # slots [3,4] in each group → Pexels
_PEXELS_MAX_RESULTS = 10   # candidates per Pexels search


def _use_pexels_for_block(idx: int) -> bool:
    """Return True if this block index should use Pexels (40% of blocks)."""
    return bool(PEXELS_API_KEY) and (idx % _PEXELS_SLOT_MOD >= _PEXELS_SLOT_FROM)


# ---------------------------------------------------------------------------
# Gemini Image Generation
# ---------------------------------------------------------------------------

def _generate_gemini_image(prompt: str, dest: Path) -> bool:
    """Generate base image via Gemini API. Save as PNG."""
    if not GEMINI_API_KEY:
        print("[VISION]     [!] GEMINI_API_KEY missing, skipping image generation.")
        return False

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        enhanced_prompt = (
            f"Photorealistic, cinematic, 16:9 aspect ratio, high detail, "
            f"documentary style: {prompt}"
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=enhanced_prompt,
            config=genai.types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        if response.candidates:
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    dest.write_bytes(part.inline_data.data)
                    return True

        print("[VISION]     [!] Gemini returned no image")
        return False

    except Exception as e:
        err_str = str(e)
        if "503" in err_str or "UNAVAILABLE" in err_str:
            print("[VISION]     [!] Gemini overloaded, retrying in 10s...")
            time.sleep(10)
            try:
                return _generate_gemini_image(prompt, dest)
            except Exception:
                pass
        print(f"[VISION]     [X] Gemini image gen failed: {err_str[:200]}")
        return False


# ---------------------------------------------------------------------------
# ComfyUI API helpers
# ---------------------------------------------------------------------------

def _comfyui_available() -> bool:
    """Quick ping to check if ComfyUI is reachable."""
    if not COMFYUI_URL:
        return False
    try:
        resp = requests.get(f"{COMFYUI_URL}/system_stats", timeout=10)
        return resp.status_code == 200
    except Exception:
        return False


def _upload_file(file_path: Path) -> str | None:
    """Upload a file to ComfyUI /api/upload/image (works for audio too)."""
    if not file_path.exists():
        print(f"[VISION]     [X] File not found for upload: {file_path}")
        return None

    try:
        with open(file_path, "rb") as f:
            files = {"image": (file_path.name, f)}
            resp = requests.post(
                f"{COMFYUI_URL}/api/upload/image", files=files, timeout=60
            )
            if resp.status_code == 200:
                name = resp.json().get("name")
                print(f"[VISION]     Uploaded {file_path.name} → {name}")
                return name
            else:
                print(f"[VISION]     [X] Upload failed {resp.status_code}: {resp.text}")
                return None
    except Exception as e:
        print(f"[VISION]     [X] Upload error: {e}")
        return None


def _load_workflow(prompt: str, image_name: str | None, audio_name: str | None) -> dict:
    """Load ComfyUI API workflow from JSON and inject prompt, image, and audio."""
    workflow_path = BASE_DIR / COMFYUI_WORKFLOW
    if not workflow_path.exists():
        print(f"[VISION]     [X] Workflow JSON not found: {workflow_path}")
        return {}

    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    # Inject Prompt
    prompt_node = COMFYUI_PROMPT_NODE
    if prompt_node in workflow:
        inputs = workflow[prompt_node].get("inputs", {})
        if "value" in inputs:
            workflow[prompt_node]["inputs"]["value"] = prompt
        elif "text" in inputs:
            workflow[prompt_node]["inputs"]["text"] = prompt

    # Inject Image & Audio by searching for node types
    for node_id, node in workflow.items():
        ctype = node.get("class_type")
        if ctype == "LoadImage" and image_name:
            node["inputs"]["image"] = image_name
        elif ctype == "LoadAudio" and audio_name:
            node["inputs"]["audio"] = audio_name
            if "audioUI" in node["inputs"]:
                node["inputs"]["audioUI"] = f"/api/view?filename={audio_name}&type=input"

    return workflow


def _submit_prompt(workflow: dict) -> str | None:
    """POST workflow to ComfyUI. Returns prompt_id or None on failure."""
    client_id = str(uuid.uuid4())
    payload = {"prompt": workflow, "client_id": client_id}
    try:
        resp = requests.post(f"{COMFYUI_URL}/api/prompt", json=payload, timeout=30)
        if resp.status_code == 200:
            return resp.json().get("prompt_id")
        print(f"[VISION]     [!] ComfyUI submit error {resp.status_code}: {resp.text[:200]}")
        return None
    except Exception as e:
        print(f"[VISION]     [!] ComfyUI submit exception: {e}")
        return None


def _poll_until_done(prompt_id: str, timeout: int = COMFYUI_TIMEOUT) -> dict | None:
    """Poll /api/history/{id} until job finishes. Returns output dict or None."""
    deadline = time.time() + timeout
    poll_interval = 3
    print(f"[VISION]     Polling ComfyUI job {prompt_id[:8]}...", end="", flush=True)

    while time.time() < deadline:
        try:
            resp = requests.get(
                f"{COMFYUI_URL}/api/history/{prompt_id}", timeout=15
            )
            if resp.status_code == 200:
                history = resp.json()
                if prompt_id in history:
                    job = history[prompt_id]
                    status = job.get("status", {})
                    if status.get("completed"):
                        print(" done")
                        return job.get("outputs", {})
                    elif status.get("status_str") == "error":
                        print(" ERROR")
                        msgs = status.get("messages", [])
                        print(f"[VISION]     [X] ComfyUI job error: {msgs}")
                        return None
        except Exception:
            pass
        print(".", end="", flush=True)
        time.sleep(poll_interval)

    print(f"\n[VISION]     [X] ComfyUI timeout after {timeout}s")
    return None


def _download_comfyui_output(outputs: dict, dest: Path) -> bool:
    """Find the mp4 in ComfyUI outputs and download it."""
    for node_id, node_output in outputs.items():
        for key in ("gifs", "videos", "images"):
            for item in node_output.get(key, []):
                filename = item.get("filename")
                if not filename or not filename.endswith(".mp4"):
                    continue

                params = {
                    "filename": filename,
                    "subfolder": item.get("subfolder", ""),
                    "type": item.get("type", "output"),
                }
                try:
                    resp = requests.get(
                        f"{COMFYUI_URL}/api/view",
                        params=params,
                        stream=True,
                        timeout=120,
                    )
                    if resp.status_code == 200:
                        with open(dest, "wb") as f:
                            for chunk in resp.iter_content(chunk_size=8192):
                                f.write(chunk)
                        print(f"[VISION]     Downloaded → {dest.name}")
                        return True
                except Exception as e:
                    print(f"[VISION]     [!] Download error: {e}")

    print("[VISION]     [X] No video file found in ComfyUI outputs")
    return False


def _generate_comfyui_clip(
    prompt: str, image_path: Path, audio_path: Path, dest: Path
) -> bool:
    """Full ComfyUI generation: upload inputs → submit → poll → download."""
    image_name = _upload_file(image_path)
    audio_name = _upload_file(audio_path)
    workflow = _load_workflow(prompt, image_name, audio_name)
    if not workflow:
        return False
    prompt_id = _submit_prompt(workflow)
    if not prompt_id:
        return False
    outputs = _poll_until_done(prompt_id)
    if not outputs:
        return False
    return _download_comfyui_output(outputs, dest)


# ---------------------------------------------------------------------------
# Pexels Video helpers
# ---------------------------------------------------------------------------

def _pexels_search(query: str, min_duration: float) -> list[dict]:
    """
    Search Pexels Videos API.
    Returns list of video-file dicts with 'link' and 'duration' keys,
    filtered to landscape orientation and >= min_duration.
    Sorted by quality (highest width first).
    """
    if not PEXELS_API_KEY:
        return []

    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "query": query,
        "orientation": "landscape",
        "size": "medium",
        "per_page": _PEXELS_MAX_RESULTS,
    }

    try:
        resp = requests.get(
            "https://api.pexels.com/videos/search",
            headers=headers,
            params=params,
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"[VISION]     [!] Pexels API error {resp.status_code}")
            return []

        videos = resp.json().get("videos", [])
        candidates: list[dict] = []

        for vid in videos:
            duration = vid.get("duration", 0)
            # Gather all HD/FHD video files for this result
            for vf in vid.get("video_files", []):
                w = vf.get("width", 0)
                h = vf.get("height", 0)
                link = vf.get("link", "")
                quality = vf.get("quality", "")
                if not link:
                    continue
                # Prefer HD (1280×720) or higher, landscape
                if w >= 1280 and h <= w:
                    candidates.append({
                        "link": link,
                        "duration": duration,
                        "width": w,
                        "height": h,
                        "quality": quality,
                    })

        # Sort: clips that fully cover needed duration first, then by width
        candidates.sort(key=lambda c: (c["duration"] >= min_duration, c["width"]), reverse=True)
        return candidates

    except Exception as exc:
        print(f"[VISION]     [!] Pexels search error: {exc}")
        return []


def _download_file(url: str, dest: Path) -> bool:
    """Download any URL to dest. Returns True on success."""
    try:
        resp = requests.get(url, stream=True, timeout=120)
        if resp.status_code != 200:
            return False
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception:
        return False


def _get_video_duration(path: Path) -> float:
    """Use ffprobe to get video duration in seconds."""
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                str(path),
            ],
            capture_output=True,
            check=True,
        )
        info = json.loads(result.stdout)
        return float(info["format"]["duration"])
    except Exception:
        return 0.0


def _fetch_pexels_for_block(query: str, duration: float, dest: Path) -> bool:
    """
    Fetch Pexels clips for `query` and produce a clip that covers `duration`
    WITHOUT looping. If one clip is too short, concatenate additional clips
    from the same search until we have enough footage.

    Returns True if dest was created successfully.
    """
    print(f"[VISION]     → Searching Pexels: '{query}' (need {duration:.1f}s)")
    candidates = _pexels_search(query, duration)

    if not candidates:
        print("[VISION]     [!] No Pexels results found")
        return False

    temp_clips: list[Path] = []
    accumulated = 0.0
    used_urls: set[str] = set()

    # Download clips until we have enough total duration
    for candidate in candidates:
        if candidate["link"] in used_urls:
            continue
        if accumulated >= duration:
            break

        clip_path = TEMP_DIR / f"pexels_{len(temp_clips):03d}_{uuid.uuid4().hex[:6]}.mp4"
        print(
            f"[VISION]       Downloading Pexels clip "
            f"({candidate['width']}×{candidate['height']}, "
            f"{candidate['duration']}s)..."
        )
        if _download_file(candidate["link"], clip_path):
            actual_dur = _get_video_duration(clip_path)
            if actual_dur > 0:
                temp_clips.append(clip_path)
                accumulated += actual_dur
                used_urls.add(candidate["link"])
                print(f"[VISION]       Got {actual_dur:.1f}s — total: {accumulated:.1f}s / {duration:.1f}s needed")
            else:
                clip_path.unlink(missing_ok=True)
        else:
            print("[VISION]       [!] Download failed, trying next...")

    if not temp_clips:
        print("[VISION]     [X] Could not download any Pexels clips")
        return False

    if accumulated < duration:
        print(
            f"[VISION]     [!] Only {accumulated:.1f}s of footage available "
            f"(needed {duration:.1f}s). Using what we have."
        )

    # Concatenate clips if we have more than one
    if len(temp_clips) == 1:
        concat_path = temp_clips[0]
    else:
        concat_path = TEMP_DIR / f"pexels_concat_{uuid.uuid4().hex[:8]}.mp4"
        concat_list = TEMP_DIR / f"concat_list_{uuid.uuid4().hex[:8]}.txt"
        concat_list.write_text(
            "\n".join(f"file '{p.resolve()}'" for p in temp_clips),
            encoding="utf-8",
        )
        try:
            subprocess.run(
                [
                    "ffmpeg", "-y",
                    "-f", "concat", "-safe", "0",
                    "-i", str(concat_list),
                    "-c", "copy",
                    str(concat_path),
                ],
                check=True,
                capture_output=True,
            )
            concat_list.unlink(missing_ok=True)
        except subprocess.CalledProcessError as e:
            print(f"[VISION]     [X] ffmpeg concat failed: {e.stderr.decode()[:300]}")
            concat_list.unlink(missing_ok=True)
            return False

    # Trim to exact duration (no stream_loop — we already have enough footage)
    ok = _trim_clip_exact(concat_path, dest, duration)

    # Cleanup temp files
    for p in temp_clips:
        if p != concat_path:
            p.unlink(missing_ok=True)
    if concat_path != dest:
        concat_path.unlink(missing_ok=True)

    return ok


# ---------------------------------------------------------------------------
# FFmpeg helpers
# ---------------------------------------------------------------------------

def _trim_clip_exact(src: Path, dest: Path, duration: float) -> bool:
    """
    Trim video to exact duration.
    NOTE: Does NOT use -stream_loop. If src is shorter than duration,
    the output will simply be shorter (caller handles this gracefully).
    """
    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(src),
                "-t", str(duration),
                "-vf", (
                    "scale=1920:1080:force_original_aspect_ratio=decrease,"
                    "pad=1920:1080:(ow-iw)/2:(oh-ih)/2"
                ),
                "-c:v", "libx264", "-preset", "fast", "-an",
                str(dest),
            ],
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"[VISION]     [X] ffmpeg trim failed: {e.stderr.decode()[:200]}")
        return False


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def fetch_visuals() -> list[Path]:
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Clean clips dir
    for old in CLIPS_DIR.glob("clip_*.mp4"):
        old.unlink()
    for old in CLIPS_DIR.glob("raw_*.*"):
        old.unlink()

    blocks = data["blocks"]

    # ── Require ComfyUI ────────────────────────────────────────────────────
    if not _comfyui_available():
        raise RuntimeError(
            f"[VISION] ✗ ComfyUI is not reachable at {COMFYUI_URL!r}.\n"
            "Make sure your RunPod pod is running and COMFYUI_URL is set correctly in .env."
        )

    print(f"[VISION] ✓ ComfyUI reachable at {COMFYUI_URL}")
    ai_count = sum(1 for b in blocks if not _use_pexels_for_block(b["block_id"]))
    px_count = len(blocks) - ai_count
    print(f"[VISION]   Mix plan: {ai_count} AI clips / {px_count} Pexels clips "
          f"({len(blocks)} total, ~60/40)")

    clips: list[Path] = []

    for block in blocks:
        idx = block["block_id"]
        final_dest = CLIPS_DIR / f"clip_{idx:03d}.mp4"
        prompt = block.get("visual_prompt", block.get("pexels_query", "space documentary"))
        pexels_query = block.get("pexels_query", prompt)
        duration = block.get("voice_duration_sec", 15.0)
        use_pexels = _use_pexels_for_block(idx)

        source_label = "Pexels" if use_pexels else "ComfyUI AI"
        print(f"\n[VISION] Block {idx:03d} | {duration:.1f}s | [{source_label}] | \"{prompt[:55]}...\"")

        success = False

        if use_pexels:
            # ── Pexels path ──────────────────────────────────────────────
            success = _fetch_pexels_for_block(pexels_query, duration, final_dest)
            if not success:
                print(f"[VISION]   [!] Pexels failed → falling back to ComfyUI AI")
                success = _generate_ai_clip(idx, prompt, duration, final_dest)
        else:
            # ── AI (ComfyUI) path ─────────────────────────────────────────
            success = _generate_ai_clip(idx, prompt, duration, final_dest)
            if not success and PEXELS_API_KEY:
                print(f"[VISION]   [!] AI failed → falling back to Pexels")
                success = _fetch_pexels_for_block(pexels_query, duration, final_dest)

        if success and final_dest.exists():
            clips.append(final_dest)
            print(f"[VISION]   ✓ clip_{idx:03d}.mp4 ({duration:.1f}s) [{source_label}]")
        else:
            print(f"[VISION]   [X] Block {idx:03d} failed — skipping")

    print(f"\n[VISION] ✓ Done: {len(clips)}/{len(blocks)} clips ready")
    return clips


def _generate_ai_clip(idx: int, prompt: str, duration: float, final_dest: Path) -> bool:
    """Run full ComfyUI AI generation for one block."""
    image_path = CLIPS_DIR / f"raw_image_{idx:03d}.png"
    audio_path = TEMP_DIR / f"voice_block_{idx:03d}.mp3"
    raw_vid_dest = CLIPS_DIR / f"raw_video_{idx:03d}.mp4"

    # 1. Generate base image via Gemini
    print("[VISION]   → Generating base image via Gemini...")
    if not _generate_gemini_image(prompt, image_path):
        print(f"[VISION]   [X] Gemini image failed for block {idx}")
        return False

    # 2. Upload inputs and trigger ComfyUI
    print("[VISION]   → Submitting to ComfyUI (Image + Audio)...")
    if not _generate_comfyui_clip(prompt, image_path, audio_path, raw_vid_dest):
        print(f"[VISION]   [X] ComfyUI generation failed for block {idx}")
        return False

    # 3. Trim to exact voice duration (no looping)
    result = _trim_clip_exact(raw_vid_dest, final_dest, duration)
    raw_vid_dest.unlink(missing_ok=True)
    return result


if __name__ == "__main__":
    fetch_visuals()
