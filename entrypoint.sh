#!/bin/bash
set -e

echo "============================================"
echo "  AI Video Generator – RunPod Container"
echo "============================================"

# ── Create persistent directories in the volume ──
# RunPod mounts /workspace as the persistent disk.
# Everything here survives Pod pause/resume.
mkdir -p /workspace/n8n
mkdir -p /workspace/credentials
mkdir -p /workspace/output

# Link credentials folder into the app so scripts find token.json etc.
ln -sfn /workspace/credentials /app/youtube_bot/credentials

# If a token.json exists in the volume, symlink it where the publisher expects it
if [ -f /workspace/credentials/token.json ]; then
    ln -sfn /workspace/credentials/token.json /app/youtube_bot/token.json
    echo "[SETUP] token.json linked from /workspace/credentials/"
fi

# If a .env file exists in the volume, use it
if [ -f /workspace/.env ]; then
    cp /workspace/.env /app/youtube_bot/.env
    echo "[SETUP] .env loaded from /workspace/"
else
    echo "[SETUP] WARNING: No .env found at /workspace/.env — API keys will be missing!"
    echo "[SETUP]          Upload your .env file to /workspace/.env via RunPod File Browser."
fi

# If a client_secret.json exists in the volume, link it
if [ -f /workspace/credentials/client_secret.json ]; then
    ln -sfn /workspace/credentials/client_secret.json /app/youtube_bot/client_secret.json
    echo "[SETUP] client_secret.json linked from /workspace/credentials/"
fi

# ── Start FastAPI wrapper (background) ──
echo ""
echo "[API] Starting FastAPI on port 8000..."
cd /app/youtube_bot
uvicorn api:app --host 0.0.0.0 --port 8000 --log-level info > /var/log/api.log 2>&1 &
API_PID=$!
echo "[API] FastAPI PID: $API_PID"

# ── Start n8n (background) ──
echo ""
echo "[N8N] Starting n8n on port 5678..."
n8n start > /var/log/n8n.log 2>&1 &
N8N_PID=$!
echo "[N8N] n8n PID: $N8N_PID"

echo ""
echo "============================================"
echo "  Services running:"
echo "  • n8n:    http://0.0.0.0:5678"
echo "  • FastAPI: http://0.0.0.0:8000"
echo "  • API Docs: http://0.0.0.0:8000/docs"
echo "============================================"
echo ""

# ── Tail both logs so Docker keeps the container alive ──
tail -f /var/log/n8n.log /var/log/api.log
