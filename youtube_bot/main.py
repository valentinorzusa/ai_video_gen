"""
main.py -- The Orchestrator
Runs the full pipeline sequentially:
  01_brain   -> data.json
  02_voice   -> voiceover.mp3
  03_vision  -> clips/ (Pexels + Gemini AI images)
  04_composer -> final_render.mp4 (vignette + crossfaded music + LUFS)
  05_publisher -> YouTube upload (auto-publish or --preview)
  06_shorts  -> YouTube Shorts (optional, --shorts flag)

Flags:
  --preview     Upload as PRIVATE (for testing/review)
  --no-upload   Skip upload entirely
  --shorts      Generate + upload Shorts after main video
  --shorts-only Generate Shorts from existing final_render.mp4
  --dry-run     Skip all uploads (applies to shorts too)
"""
import importlib
import json
import subprocess
import sys
import time

# Force UTF-8 output on Windows (avoids CP1252 UnicodeEncodeError for ✓ → ✗ etc.)
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8")

from config import DATA_JSON, VOICEOVER_PATH, FINAL_RENDER, OUTPUT_DIR

THUMBNAIL_PATH = OUTPUT_DIR / "thumbnail.png"


def _extract_thumbnail():
    """Extract a high-quality frame from the final video as thumbnail."""
    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-ss", "30",
                "-i", str(FINAL_RENDER),
                "-vframes", "1",
                "-q:v", "2",
                str(THUMBNAIL_PATH),
            ],
            check=True,
            capture_output=True,
        )
        print(f"[THUMBNAIL] [OK] Extracted -> {THUMBNAIL_PATH}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[THUMBNAIL] [!] Failed: {e.stderr.decode()[:200]}")
        return False


def run_pipeline(topic: str, preview: bool = False, upload: bool = True, shorts: bool = False):
    """Execute full pipeline."""
    start = time.time()
    print("=" * 60)
    print(f"  AI VIDEO GENERATOR -- Pipeline Start")
    print(f"  Topic: {topic[:80]}")
    if preview:
        print(f"  Mode: PREVIEW (private upload)")
    print("=" * 60)

    # -- Step 1: Brain --
    print("\n[1/5] BRAIN -- Generating script...")
    brain = importlib.import_module("01_brain")
    data = brain.generate_script(topic)

    # -- Step 2: Voice --
    print("\n[2/5] VOICE -- Generating voiceover...")
    voice = importlib.import_module("02_voice")
    voice.generate_voiceover()

    # -- Step 3: Vision --
    print("\n[3/5] VISION -- Fetching visuals (Pexels + Gemini)...")
    vision = importlib.import_module("03_vision")
    vision.fetch_visuals()

    # -- Step 4: Composer --
    print("\n[4/5] COMPOSER -- Assembling video...")
    composer = importlib.import_module("04_composer")
    composer.compose_video()

    # -- Post-render: Thumbnail --
    print()
    _extract_thumbnail()

    elapsed = time.time() - start
    print(f"\n[RENDER] [OK] Video rendered in {elapsed/60:.1f} minutes")
    print(f"[RENDER] File: {FINAL_RENDER}")

    # -- Step 5: Upload --
    video_id = None
    if upload:
        print("\n[5/5] PUBLISHER -- Uploading to YouTube...")
        publisher = importlib.import_module("05_publisher")
        video_id = publisher.upload_video(preview=preview)
    else:
        print("\n[5/5] PUBLISHER -- Skipped (--no-upload)")

    # -- Step 6: Shorts (optional) --
    if shorts:
        print("\n[BONUS] SHORTS -- Generating YouTube Shorts...")
        shorts_mod = importlib.import_module("06_shorts")
        shorts_mod.generate_shorts(full_video_id=video_id, upload=upload and not preview)

    # -- Summary --
    elapsed = time.time() - start
    print(f"\n{'=' * 60}")
    print(f"  [OK] Pipeline complete in {elapsed/60:.1f} minutes")
    print(f"  Video:  {FINAL_RENDER.name}")
    print(f"  Thumb:  thumbnail.png")
    if video_id:
        print(f"  YouTube: https://youtube.com/watch?v={video_id}")
        if preview:
            print(f"  Status:  PRIVATE (preview mode)")
        else:
            print(f"  Status:  PUBLIC")
    print("=" * 60)

    return video_id


def run_shorts(upload: bool = True):
    """Generate YouTube Shorts from existing final_render.mp4."""
    shorts = importlib.import_module("06_shorts")
    shorts.generate_shorts(upload=upload)


if __name__ == "__main__":
    args = sys.argv[1:]
    flags = [a for a in args if a.startswith("--")]
    positional = [a for a in args if not a.startswith("--")]

    preview = "--preview" in flags
    no_upload = "--no-upload" in flags or "--dry-run" in flags
    do_shorts = "--shorts" in flags

    # --shorts-only: just generate shorts from existing video
    if "--shorts-only" in flags:
        run_shorts(upload=not no_upload)
        sys.exit(0)

    # Normal pipeline
    topic = " ".join(positional) if positional else (
        "The Hidden Ocean of Europa: Could Life Exist Beneath the Ice?"
    )
    run_pipeline(
        topic,
        preview=preview,
        upload=not no_upload,
        shorts=do_shorts,
    )
