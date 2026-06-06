"""
03_vision.py -- The Scout/Generator (ComfyUI IA2V Edition)
Reads data.json. For each block:
  1. Generates a base image using Gemini
  2. Uploads the image and the block's audio (from 02_voice.py) to ComfyUI
  3. Injects the prompt, image filename, and audio filename into the workflow
  4. Polls ComfyUI for the resulting video clip
  5. Trims/pads the video to exactly match the voice duration
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
)

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

        print(f"[VISION]     [!] Gemini returned no image")
        return False

    except Exception as e:
        err_str = str(e)
        if "503" in err_str or "UNAVAILABLE" in err_str:
            print(f"[VISION]     [!] Gemini overloaded, retrying in 10s...")
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
            # ComfyUI expects the field name to be "image" for all uploads
            files = {"image": (file_path.name, f)}
            resp = requests.post(f"{COMFYUI_URL}/api/upload/image", files=files, timeout=60)
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
            # If the node also has audioUI, we can update it just in case
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
            resp = requests.get(f"{COMFYUI_URL}/api/history/{prompt_id}", timeout=15)
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
        for key in ('gifs', 'videos', 'images'):
            for item in node_output.get(key, []):
                filename = item.get('filename')
                if not filename or not filename.endswith('.mp4'):
                    continue
                
                params = {
                    "filename": filename,
                    "subfolder": item.get("subfolder", ""),
                    "type": item.get("type", "output"),
                }
                try:
                    resp = requests.get(f"{COMFYUI_URL}/api/view", params=params, stream=True, timeout=120)
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


def _generate_comfyui_clip(prompt: str, image_path: Path, audio_path: Path, dest: Path) -> bool:
    """Full ComfyUI generation: upload inputs → submit → poll → download."""
    
    # 1. Upload files
    image_name = _upload_file(image_path)
    audio_name = _upload_file(audio_path)
    
    # 2. Build workflow
    workflow = _load_workflow(prompt, image_name, audio_name)
    if not workflow:
        return False
        
    # 3. Submit
    prompt_id = _submit_prompt(workflow)
    if not prompt_id:
        return False

    # 4. Poll & Download
    outputs = _poll_until_done(prompt_id)
    if not outputs:
        return False
    return _download_comfyui_output(outputs, dest)


# ---------------------------------------------------------------------------
# Download helper (used for any direct URL, kept for future use)
# ---------------------------------------------------------------------------

def _download_file(url: str, dest: Path) -> bool:
    try:
        resp = requests.get(url, stream=True, timeout=120)
        if resp.status_code != 200: return False
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192): f.write(chunk)
        return True
    except Exception: return False


# ---------------------------------------------------------------------------
# FFmpeg helpers
# ---------------------------------------------------------------------------

def _trim_clip(src: Path, dest: Path, duration: float) -> bool:
    """Trim/loop video clip to exact duration via ffmpeg."""
    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-stream_loop", "-1",
                "-i", str(src),
                "-t", str(duration),
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
                       "pad=1920:1080:(ow-iw)/2:(oh-ih)/2",
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
    for old in CLIPS_DIR.glob("clip_*.mp4"): old.unlink()
    for old in CLIPS_DIR.glob("raw_*.*"): old.unlink()

    blocks = data["blocks"]

    # ── Require ComfyUI — no fallback ─────────────────────────────────────
    if not _comfyui_available():
        raise RuntimeError(
            f"[VISION] ✗ ComfyUI is not reachable at {COMFYUI_URL!r}.\n"
            "Make sure your RunPod pod is running and COMFYUI_URL is set correctly in .env."
        )

    print(f"[VISION] ✓ ComfyUI reachable at {COMFYUI_URL}")
    print(f"[VISION]   Generating ALL clips via ComfyUI (Gemini image → LTX-2.3 video)")

    clips: list[Path] = []

    for block in blocks:
        idx = block["block_id"]
        final_dest = CLIPS_DIR / f"clip_{idx:03d}.mp4"
        prompt = block.get("visual_prompt", block.get("pexels_query", "space documentary"))
        duration = block.get("voice_duration_sec", 15.0)

        print(f"\n[VISION] Block {idx:03d} | {duration:.1f}s | \"{prompt[:60]}...\"")

        image_path = CLIPS_DIR / f"raw_image_{idx:03d}.png"
        audio_path = TEMP_DIR / f"voice_block_{idx:03d}.mp3"
        raw_vid_dest = CLIPS_DIR / f"raw_video_{idx:03d}.mp4"

        # 1. Generate base image via Gemini
        print(f"[VISION]   → Generating base image via Gemini...")
        if not _generate_gemini_image(prompt, image_path):
            print(f"[VISION]   [X] Gemini image failed for block {idx} — skipping")
            continue

        # 2. Upload inputs and trigger ComfyUI
        print(f"[VISION]   → Submitting to ComfyUI (Image + Audio)...")
        if not _generate_comfyui_clip(prompt, image_path, audio_path, raw_vid_dest):
            print(f"[VISION]   [X] ComfyUI generation failed for block {idx} — skipping")
            continue

        # 3. Trim/pad to exact voice duration
        if _trim_clip(raw_vid_dest, final_dest, duration):
            clips.append(final_dest)
            raw_vid_dest.unlink(missing_ok=True)
            print(f"[VISION]   ✓ clip_{idx:03d}.mp4 ({duration:.1f}s)")
        else:
            print(f"[VISION]   [X] ffmpeg trim failed for block {idx} — skipping")

    print(f"\n[VISION] ✓ Done: {len(clips)}/{len(blocks)} clips ready")
    return clips

if __name__ == "__main__":
    fetch_visuals()
