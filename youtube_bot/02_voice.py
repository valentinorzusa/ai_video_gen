"""
02_voice.py — The Voice Actor
Generates one mp3 per script block → measures exact duration per block.
Writes per-block durations back into data.json for use by 03_vision.py.
Also concatenates all blocks into a single voiceover.mp3.
"""
import json
import subprocess
from pathlib import Path

import requests

from config import (
    DATA_JSON,
    ELEVENLABS_API_KEY,
    ELEVENLABS_MODEL,
    ELEVENLABS_VOICE_ID,
    TEMP_DIR,
    VOICEOVER_PATH,
)


def _tts_block(text: str, output_path: Path) -> bool:
    """Single TTS API call → mp3 file."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "model_id": ELEVENLABS_MODEL,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=120)
    if resp.status_code == 200:
        output_path.write_bytes(resp.content)
        return True
    print(f"[VOICE] ✗ ElevenLabs error {resp.status_code}: {resp.text[:200]}")
    return False


def _get_duration(mp3_path: Path) -> float:
    """Get audio duration in seconds via ffprobe."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(mp3_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def _concat_mp3(block_files: list[Path], output: Path) -> None:
    """Concatenate per-block mp3s into final voiceover.mp3 via ffmpeg."""
    list_file = TEMP_DIR / "concat_list.txt"
    with open(list_file, "w") as f:
        for bf in block_files:
            f.write(f"file '{bf.resolve()}'\n")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
         "-i", str(list_file), "-c", "copy", str(output)],
        check=True,
        capture_output=True,
    )


def generate_voiceover() -> Path:
    """
    Generate one mp3 per block → measure exact duration → write back to data.json.
    Concatenate all blocks → voiceover.mp3.
    """
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    blocks = data["blocks"]
    print(f"[VOICE] Generating TTS for {len(blocks)} blocks...")

    block_files: list[Path] = []
    total_duration = 0.0

    for block in blocks:
        idx = block["block_id"]
        block_path = TEMP_DIR / f"voice_block_{idx:03d}.mp3"

        ok = _tts_block(block["voiceover"], block_path)
        if not ok:
            raise RuntimeError(f"TTS failed on block {idx}")

        duration = _get_duration(block_path)
        block["voice_duration_sec"] = round(duration, 3)
        total_duration += duration
        block_files.append(block_path)
        print(f"[VOICE]   block {idx}: {duration:.1f}s ✓")

    # Write durations back to data.json
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[VOICE] ✓ Durations written to data.json (total: {total_duration/60:.1f}min)")

    # Concat all blocks
    if len(block_files) == 1:
        import shutil
        shutil.copy(block_files[0], VOICEOVER_PATH)
    else:
        _concat_mp3(block_files, VOICEOVER_PATH)

    print(f"[VOICE] ✓ Voiceover saved → {VOICEOVER_PATH}")
    return VOICEOVER_PATH


if __name__ == "__main__":
    generate_voiceover()
