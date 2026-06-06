# ============================================================
#  AI Video Generator – RunPod Deployment
#  Base: PyTorch 2.1.2 + CUDA 12.1 (GPU support for Whisper)
#  Services: n8n (port 5678) + FastAPI (port 8000)
# ============================================================
FROM pytorch/pytorch:2.1.2-cuda12.1-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    N8N_PORT=5678 \
    N8N_PROTOCOL=http \
    N8N_HOST=0.0.0.0 \
    # Persist n8n data inside the mounted volume
    N8N_USER_FOLDER=/workspace/n8n \
    # Disable n8n update checks (faster startup)
    N8N_DIAGNOSTICS_ENABLED=false \
    N8N_VERSION_NOTIFICATIONS_ENABLED=false

# ── 1. System dependencies ──────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    fonts-dejavu \
    git \
    curl \
    ca-certificates \
    gnupg \
    wget \
    && rm -rf /var/lib/apt/lists/*

# ── 2. Node.js 20.x (required for n8n) ──────────────────────
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
       | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" \
       | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# ── 3. n8n (global install) ──────────────────────────────────
RUN npm install -g n8n --unsafe-perm

# ── 4. Python workspace ──────────────────────────────────────
WORKDIR /app

COPY youtube_bot/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install FastAPI + Uvicorn for the API wrapper
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic

# ── 5. Pre-download Whisper 'base' model (avoids cold-start lag) ──
RUN python -c "import whisper; whisper.load_model('base')"

# ── 6. Copy project files ────────────────────────────────────
COPY youtube_bot/ ./youtube_bot/
COPY resources/   ./resources/

# ── 7. Install Komika Axis font system-wide (needed for Shorts subtitles) ──
RUN mkdir -p /usr/share/fonts/truetype/custom \
    && cp resources/KOMIKAX_.ttf /usr/share/fonts/truetype/custom/komikax.ttf \
    && fc-cache -f -v

# ── 8. Startup script ────────────────────────────────────────
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5678 8000

ENTRYPOINT ["/entrypoint.sh"]
