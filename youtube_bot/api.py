"""
api.py — FastAPI wrapper for the YouTube Bot pipeline.

Exposes HTTP endpoints so n8n can trigger and monitor video generation
without needing direct shell access.

Endpoints:
  POST /generate          → Start a full video generation job
  GET  /tasks/{task_id}   → Poll job status and progress
  GET  /health            → Health check (n8n can ping this)
  GET  /docs              → Swagger UI (auto-generated)
"""
import uuid
import subprocess
import sys
import os
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel

# ── App ──────────────────────────────────────────────────────
app = FastAPI(
    title="AI Video Generator API",
    description="Controls the YouTube Bot pipeline. Trigger video generation and poll status.",
    version="1.0.0",
)

# ── In-memory task store ─────────────────────────────────────
# Survives as long as the FastAPI process is running.
# If you need persistence across restarts, swap for a JSON file or SQLite.
tasks: dict[str, dict] = {}

# ── Paths ─────────────────────────────────────────────────────
BOT_DIR = Path(__file__).resolve().parent


# ── Models ───────────────────────────────────────────────────
class GenerationRequest(BaseModel):
    topic: str
    preview: bool = False          # True → upload as PRIVATE (safe for testing)
    upload: bool = True            # False → skip YouTube upload entirely
    shorts: bool = False           # True → also generate YouTube Shorts
    dry_run: bool = False          # True → skip all uploads (local render only)

class TaskStatus(BaseModel):
    task_id: str
    status: str                    # queued | running | completed | failed
    progress: str
    output: Optional[str] = None   # Last 2000 chars of stdout on success
    error: Optional[str] = None    # Last 2000 chars of stderr on failure


# ── Background worker ────────────────────────────────────────
def _run_pipeline(task_id: str, req: GenerationRequest):
    """Execute main.py as a subprocess and track progress."""
    tasks[task_id]["status"] = "running"
    tasks[task_id]["progress"] = "Starting pipeline…"

    # Build the command
    cmd = [sys.executable, str(BOT_DIR / "main.py"), req.topic]
    if req.preview:
        cmd.append("--preview")
    if not req.upload or req.dry_run:
        cmd.append("--no-upload")
    if req.shorts:
        cmd.append("--shorts")

    tasks[task_id]["progress"] = f"Running: {' '.join(cmd[2:])}"

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(BOT_DIR),
            env={**os.environ, "PYTHONPATH": str(BOT_DIR)},
        )

        if result.returncode == 0:
            tasks[task_id] = {
                "status": "completed",
                "progress": "Pipeline finished successfully ✓",
                "output": result.stdout[-3000:],   # last 3000 chars
                "error": None,
            }
        else:
            tasks[task_id] = {
                "status": "failed",
                "progress": f"Pipeline exited with code {result.returncode}",
                "output": result.stdout[-1000:],
                "error": result.stderr[-3000:],
            }

    except Exception as exc:
        tasks[task_id] = {
            "status": "failed",
            "progress": "Unexpected error launching pipeline",
            "output": None,
            "error": str(exc),
        }


# ── Endpoints ────────────────────────────────────────────────
@app.get("/health")
def health():
    """Simple health check for n8n and monitoring tools."""
    return {"status": "ok", "service": "ai-video-generator"}


@app.post("/generate", response_model=TaskStatus, status_code=202)
def generate_video(req: GenerationRequest, background_tasks: BackgroundTasks):
    """
    Kick off a full video generation job in the background.
    Returns a task_id immediately — poll /tasks/{task_id} to track progress.
    """
    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "status": "queued",
        "progress": "Job queued, will start shortly…",
        "output": None,
        "error": None,
    }
    background_tasks.add_task(_run_pipeline, task_id, req)
    return {"task_id": task_id, **tasks[task_id]}


@app.get("/tasks/{task_id}", response_model=TaskStatus)
def get_task(task_id: str):
    """Poll the status of a generation job."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task '{task_id}' not found")
    return {"task_id": task_id, **tasks[task_id]}


@app.get("/tasks")
def list_tasks():
    """List all known tasks (for debugging)."""
    return [{"task_id": k, **v} for k, v in tasks.items()]
