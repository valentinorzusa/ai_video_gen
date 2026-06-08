#!/bin/bash
# pod_setup.sh — Runs inside the RunPod pod after boot.
# Called automatically by runpod_launch.py via SSH.
# DO NOT run this manually on your local machine.

set -e

echo ""
echo "============================================================"
echo "  AI Video Generator — Pod Auto-Setup"
echo "============================================================"

REPO_DIR="/workspace/ai_video_gen"
COMFY_DIR="/workspace/ComfyUI"
WORKFLOW_SRC="$REPO_DIR/youtube_bot/47d245c34a7d.json"
WORKFLOW_DST="$COMFY_DIR/user/default/workflows/ltxv_workflow.json"

# 1. Clone / update the repo
echo ""
echo "[1/5] Cloning repo..."
if [ -d "$REPO_DIR/.git" ]; then
    echo "      Repo exists — pulling latest..."
    cd "$REPO_DIR" && git pull
else
    git clone --depth=1 -b main \
        https://github.com/valentinorzusa/ai_video_gen.git \
        "$REPO_DIR"
fi

# 2. Install Python deps for the pipeline
echo ""
echo "[2/5] Installing Python dependencies..."
pip install -q fastapi uvicorn python-dotenv \
    google-generativeai google-genai \
    elevenlabs requests moviepy

# 3. Download LTXV-13B models
echo ""
echo "[3/5] Downloading LTXV models (~20GB) ..."
bash "$REPO_DIR/youtube_bot/runpod_comfyui_setup.sh"

# 4. Install ComfyUI workflow
echo ""
echo "[4/5] Installing ComfyUI workflow..."
mkdir -p "$(dirname "$WORKFLOW_DST")"
if [ -f "$WORKFLOW_SRC" ]; then
    cp "$WORKFLOW_SRC" "$WORKFLOW_DST"
    echo "      Workflow copied → $WORKFLOW_DST"
else
    echo "      [WARN] Workflow JSON not found at $WORKFLOW_SRC"
fi

# 5. Start FastAPI wrapper on port 8000
echo ""
echo "[5/5] Starting FastAPI on port 8000..."
if [ -f /workspace/.env ]; then
    cp /workspace/.env "$REPO_DIR/youtube_bot/.env"
    echo "      .env loaded from /workspace/.env"
fi
cd "$REPO_DIR/youtube_bot"
nohup uvicorn api:app --host 0.0.0.0 --port 8000 \
    > /var/log/fastapi_pod.log 2>&1 &
echo "      FastAPI PID: $!"

echo ""
echo "============================================================"
echo "  Setup complete."
echo "  ComfyUI:  http://0.0.0.0:8188"
echo "  FastAPI:  http://0.0.0.0:8000"
echo "  Docs:     http://0.0.0.0:8000/docs"
echo "============================================================"
echo ""
