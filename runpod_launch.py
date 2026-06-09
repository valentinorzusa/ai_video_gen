"""
runpod_launch.py — RunPod Automation for AI Video Generator
============================================================
Automates the full RunPod ComfyUI pod lifecycle so you never touch the
RunPod console manually.

Usage:
    python runpod_launch.py "Europa's Hidden Ocean"
    python runpod_launch.py "Black Holes" --no-upload
    python runpod_launch.py "Mars Colonization" --shorts

Flow:
    1. Check RTX 4090 availability → fallback to RTX 3090 after 60s
    2. Create RunPod ComfyUI pod
    3. SSH → git clone repo + download LTXV models (~20GB)
    4. Wait for ComfyUI ready (models loaded)
    5. Patch local youtube_bot/.env with ComfyUI URL
    6. Run main.py pipeline locally
    7. Terminate pod (ALWAYS — even on error or Ctrl+C)
"""

import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# ── dotenv load (from youtube_bot/.env) ────────────────────────────────────
from dotenv import load_dotenv

ENV_PATH = Path(__file__).parent / "youtube_bot" / ".env"
load_dotenv(ENV_PATH)

import requests
import runpod

# ── Constants ───────────────────────────────────────────────────────────────

RUNPOD_API_KEY: str = os.getenv("RUNPOD_API_KEY", "")

# GPU fallback order — exact IDs as returned by RunPod API.
# Tries 4090 first; if unavailable after 60s, falls back to 3090.
GPU_SEQUENCE = [
    "NVIDIA GeForce RTX 4090",
    "NVIDIA GeForce RTX 3090",
]
RETRY_INTERVAL_SEC = 60       # seconds between full GPU-check cycles

POD_NAME = "ComfyUI_bot_script"
COMFYUI_PORT = 8188
FASTAPI_PORT = 8000

# Docker image used by the official RunPod ComfyUI template
COMFYUI_IMAGE = "runpod/comfyui:latest"

# GitHub repo to clone onto the pod
REPO_URL = "https://github.com/valentinorzusa/ai_video_gen.git"
REPO_BRANCH = "main"
REPO_DIR_ON_POD = "/workspace/ai_video_gen"

# Local paths
BOT_DIR = Path(__file__).parent / "youtube_bot"
WORKFLOW_JSON = BOT_DIR / "47d245c34a7d.json"

# API keys to inject as pod environment variables at creation time.
# This eliminates the need for SFTP to upload .env — the pod generates
# its own .env from these env vars via an SSH shell command.
POD_ENV_KEYS = [
    "GEMINI_API_KEY",
    "ANTHROPIC_API_KEY",
    "ELEVENLABS_API_KEY",
    "PEXELS_API_KEY",
    "ELEVENLABS_VOICE_ID",
    "YOUTUBE_CLIENT_SECRETS",
]

# How long to wait for ComfyUI to finish loading models after SSH setup
COMFYUI_READY_TIMEOUT = 1800   # 30min (20GB download + model load can be slow)
POD_START_TIMEOUT = 300        # 5min for pod to reach RUNNING
SSH_READY_TIMEOUT = 180        # 3min max to wait for SSH port to open

# ── GPU Helpers ──────────────────────────────────────────────────────────────

def _gpu_available(gpu_id: str) -> bool:
    """
    Check a specific GPU's availability using runpod.get_gpu(id).
    A GPU is considered available when RunPod lists it as offered
    on secure or community cloud with a non-zero price.
    """
    try:
        g = runpod.get_gpu(gpu_id)
        if not g:
            return False
        # Available if offered on at least one cloud tier with a real price
        secure_ok    = g.get("secureCloud")    and (g.get("securePrice")    or 0) > 0
        community_ok = g.get("communityCloud") and (g.get("communityPrice") or 0) > 0
        return bool(secure_ok or community_ok)
    except Exception as exc:
        print(f"[GPU] API error for {gpu_id!r}: {exc}")
        return False


def find_available_gpu() -> tuple[str, str]:
    """
    Check each GPU in GPU_SEQUENCE via per-GPU API call.
    Returns (gpu_id, gpu_id) — id is used directly as both display name and API id.
    Retries every RETRY_INTERVAL_SEC until one is available.
    """
    cycle = 0

    while True:
        cycle += 1
        print(f"\n[GPU] Check #{cycle} — scanning RunPod GPU availability...")

        for gpu_id in GPU_SEQUENCE:
            print(f"[GPU]   Checking {gpu_id}...", end=" ", flush=True)
            if _gpu_available(gpu_id):
                print("[OK] AVAILABLE")
                return gpu_id, gpu_id   # id == id in RunPod API
            else:
                print("[--] not available")

        # Countdown before retry
        print(f"[GPU] No GPU available. Retrying in {RETRY_INTERVAL_SEC}s "
              f"(Ctrl+C to abort)...")
        _countdown(RETRY_INTERVAL_SEC)


def _countdown(seconds: int) -> None:
    """Print a live countdown in the terminal."""
    for remaining in range(seconds, 0, -5):
        print(f"\r[GPU]   ... {remaining:3d}s remaining", end="", flush=True)
        time.sleep(min(5, remaining))
    print()


# ── Pod Management ───────────────────────────────────────────────────────────

def create_pod(gpu_id: str, gpu_name: str) -> str:
    """Create RunPod pod with ComfyUI image. Returns pod_id."""
    print(f"\n[POD] Creating pod '{POD_NAME}' on {gpu_name}...")

    # Inject API keys as pod env vars so the pod can build its own .env
    # without needing any SFTP file upload.
    env_vars = {
        k: os.getenv(k, "")
        for k in POD_ENV_KEYS
        if os.getenv(k, "")
    }
    if env_vars:
        print(f"[POD] Injecting {len(env_vars)} API keys as pod env vars")

    pod = runpod.create_pod(
        name=POD_NAME,
        image_name=COMFYUI_IMAGE,
        gpu_type_id=gpu_id,
        cloud_type="SECURE",
        support_public_ip=True,
        ports=f"{COMFYUI_PORT}/http,{FASTAPI_PORT}/http,22/tcp",
        container_disk_in_gb=80,   # ComfyUI + models (~25GB) + repo + headroom
        volume_in_gb=0,            # no persistent volume → full cleanup on terminate
        env=env_vars,
    )

    pod_id = pod["id"]
    print(f"[POD] Created: {pod_id}")
    print(f"[POD] Console: https://www.runpod.io/console/pods/{pod_id}")
    return pod_id


def wait_pod_running(pod_id: str) -> dict:
    """Poll until pod runtime is populated (= RUNNING). Returns pod dict."""
    deadline = time.time() + POD_START_TIMEOUT
    print(f"\n[POD] Waiting for pod to start", end="", flush=True)

    while time.time() < deadline:
        try:
            pod = runpod.get_pod(pod_id)
            if pod and pod.get("runtime"):
                print(" ✓ RUNNING")
                return pod
        except Exception:
            pass
        print(".", end="", flush=True)
        time.sleep(10)

    raise TimeoutError(
        f"Pod {pod_id} did not reach RUNNING within {POD_START_TIMEOUT}s. "
        f"Check https://www.runpod.io/console/pods/{pod_id}"
    )


def terminate_pod(pod_id: str) -> None:
    """Terminate pod. Logs warning if it fails so user can do it manually."""
    print(f"\n[POD] Terminating {pod_id}...")
    try:
        runpod.terminate_pod(pod_id)
        print("[POD] Terminated OK")
    except Exception as exc:
        print(f"[POD] ⚠️  Terminate call failed: {exc}")
        print(f"[POD] ⚠️  MANUALLY terminate at: "
              f"https://www.runpod.io/console/pods/{pod_id}")


def get_proxy_url(pod_id: str, port: int) -> str:
    """Build RunPod proxy URL for a given pod + port."""
    return f"https://{pod_id}-{port}.proxy.runpod.net"


def _get_ssh_details(pod: dict, pod_id: str) -> dict:
    """
    Return SSH connection details as a dict with keys:
      method   : 'full' (public IP, supports SFTP) or 'proxy' (ssh.runpod.io)
      hostname : IP address or 'ssh.runpod.io'
      port     : integer port number
      username : 'root' for full SSH, or '{pod_id}' for proxy

    Tries full SSH (public IP, TCP port 22) first.
    Falls back to RunPod proxy SSH if public port not yet available.
    """
    runtime = pod.get("runtime") or {}
    for port_info in runtime.get("ports", []):
        # Full SSH: privatePort 22, type tcp, has a real IP and public port
        if (
            port_info.get("privatePort") == 22
            and port_info.get("type", "").lower() == "tcp"
        ):
            ip = port_info.get("ip", "")
            pub_port = port_info.get("publicPort")
            if ip and pub_port:
                return {
                    "method": "full",
                    "hostname": ip,
                    "port": int(pub_port),
                    "username": "root",
                }

    # Fallback: RunPod proxy SSH (always available, no SFTP)
    # Username is the pod_id per RunPod docs basic SSH format.
    print("[SSH] Public-IP SSH port not found — falling back to RunPod proxy SSH")
    return {
        "method": "proxy",
        "hostname": "ssh.runpod.io",
        "port": 22,
        "username": pod_id,
    }


# ── SSH Setup ────────────────────────────────────────────────────────────────

def _find_ssh_key() -> Path:
    """Find the user's default SSH private key."""
    candidates = [
        Path.home() / ".ssh" / "id_ed25519",
        Path.home() / ".ssh" / "id_rsa",
        Path.home() / ".ssh" / "id_ecdsa",
    ]
    for key in candidates:
        if key.exists():
            return key
    raise FileNotFoundError(
        "No SSH private key found in ~/.ssh/. "
        "Generate one with: ssh-keygen -t ed25519\n"
        "Then add the PUBLIC key to RunPod: "
        "https://www.runpod.io/console/settings/ssh"
    )


def _ssh_exec(client, command: str, description: str = "", timeout: int = 1800) -> str:
    """Execute a command via SSH, stream output, return stdout string."""
    if description:
        print(f"\n[SSH] {description}")

    _, stdout, stderr = client.exec_command(command, timeout=timeout)

    lines = []
    for line in stdout:
        stripped = line.rstrip()
        lines.append(stripped)
        # Only print non-empty lines to keep output clean
        if stripped:
            print(f"      {stripped}")

    exit_code = stdout.channel.recv_exit_status()
    err_text = stderr.read().decode(errors="replace")

    if exit_code != 0:
        if err_text:
            print(f"[SSH] STDERR:\n{err_text[:800]}")
        raise RuntimeError(
            f"SSH command failed (exit {exit_code}): {command[:120]}"
        )

    return "\n".join(lines)


def setup_pod_via_ssh(pod: dict, pod_id: str) -> None:
    """
    SSH into pod and:
      1. Clone the repo
      2. Install Python deps
      3. Generate .env from pod env vars (no SFTP needed)
      4. Copy ComfyUI workflow from cloned repo
      5. Download LTXV models (~20GB)
      6. Start FastAPI on port 8000

    Supports both RunPod SSH methods per docs:
      - Full SSH (public IP, port 22): preferred, more reliable
      - Basic SSH (proxy via ssh.runpod.io): fallback, always available
    Both methods work the same way with paramiko for commands.
    No SFTP is used — .env is generated on the pod from env vars
    injected at pod creation time.
    """
    import paramiko

    ssh_info = _get_ssh_details(pod, pod_id)
    key_path = _find_ssh_key()

    method_label = (
        f"{ssh_info['hostname']}:{ssh_info['port']}"
        if ssh_info["method"] == "full"
        else f"proxy → {ssh_info['username']}@ssh.runpod.io"
    )
    print(f"\n[SSH] Connecting via {ssh_info['method'].upper()} SSH: {method_label}")
    print(f"[SSH] Key: {key_path.name}")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # SSH port may not open immediately after pod reaches RUNNING status —
    # retry for up to SSH_READY_TIMEOUT seconds.
    max_attempts = SSH_READY_TIMEOUT // 10
    for attempt in range(max_attempts):
        try:
            client.connect(
                hostname=ssh_info["hostname"],
                port=ssh_info["port"],
                username=ssh_info["username"],
                key_filename=str(key_path),
                timeout=20,
                banner_timeout=30,
                auth_timeout=30,
            )
            print(f"[SSH] Connected OK  (attempt {attempt + 1}/{max_attempts})")
            break
        except Exception as exc:
            if attempt == max_attempts - 1:
                raise RuntimeError(
                    f"SSH connection failed after {max_attempts} attempts.\n"
                    f"Last error: {exc}\n"
                    f"Make sure your SSH public key is added at:\n"
                    f"  https://www.runpod.io/console/user/settings  (SSH Public Keys section)"
                )
            print(
                f"[SSH] Waiting for SSH to open ({attempt + 1}/{max_attempts})...",
                end="\r", flush=True,
            )
            time.sleep(10)

    try:
        # ── 1. Clone repo ──────────────────────────────────────────────────
        _ssh_exec(
            client,
            f"git clone --depth=1 -b {REPO_BRANCH} {REPO_URL} {REPO_DIR_ON_POD} 2>&1 || "
            f"(cd {REPO_DIR_ON_POD} && git pull 2>&1)",
            description="Cloning repo from GitHub...",
        )

        # ── 2. Install Python dependencies ────────────────────────────────
        _ssh_exec(
            client,
            "pip install -q fastapi uvicorn python-dotenv "
            "google-generativeai google-genai elevenlabs requests moviepy 2>&1",
            description="Installing Python dependencies...",
        )

        # ── 3. Generate .env from pod env vars (no SFTP needed) ───────────
        # API keys were injected as pod env vars at creation time (create_pod).
        # We write them out to .env on the pod using a Python one-liner.
        env_keys = " ".join(f"'{k}'" for k in POD_ENV_KEYS)
        gen_env_cmd = (
            f"python3 -c \""
            f"import os, pathlib; "
            f"keys = [{env_keys}]; "
            f"lines = [f'{{k}}={{os.getenv(k, \"\")}}'  for k in keys if os.getenv(k)]; "
            f"pathlib.Path('{REPO_DIR_ON_POD}/youtube_bot/.env').write_text('\\n'.join(lines) + '\\n'); "
            f"print(f'Generated .env with {{len(lines)}} keys')"
            f"\""
        )
        _ssh_exec(client, gen_env_cmd, description="Generating .env from pod env vars...")

        # Also add COMFYUI_WORKFLOW so the pipeline finds the right JSON
        _ssh_exec(
            client,
            f"echo 'COMFYUI_WORKFLOW=47d245c34a7d.json' >> {REPO_DIR_ON_POD}/youtube_bot/.env && "
            f"echo 'COMFYUI_PROMPT_NODE=267:266' >> {REPO_DIR_ON_POD}/youtube_bot/.env",
        )

        # ── 5. Download LTXV models (~20GB) ───────────────────────────────
        print("\n[SSH] Downloading LTXV models (~20GB) — takes several minutes...")
        _ssh_exec(
            client,
            f"bash {REPO_DIR_ON_POD}/youtube_bot/runpod_comfyui_setup.sh 2>&1",
            description="Running LTXV model setup script...",
            timeout=3600,  # 1hr max — model downloads can be slow
        )

        print("[SSH] Pod setup complete - done")

    finally:
        client.close()
        print("[SSH] Disconnected")


# ── ComfyUI Readiness ────────────────────────────────────────────────────────

def wait_comfyui_ready(comfyui_url: str) -> None:
    """
    Poll ComfyUI /system_stats until it responds with 200.
    The pod needs time to finish loading models after download.
    """
    deadline = time.time() + COMFYUI_READY_TIMEOUT
    print(f"\n[COMFYUI] Waiting for ComfyUI at {comfyui_url}", end="", flush=True)

    while time.time() < deadline:
        try:
            resp = requests.get(f"{comfyui_url}/system_stats", timeout=8)
            if resp.status_code == 200:
                print(" [READY]")
                data = resp.json()
                if "system" in data:
                    print(f"[COMFYUI] {data['system'].get('python_version', '')} | "
                          f"VRAM: {data['devices'][0].get('vram_total', '?')}MB")
                return
        except Exception:
            pass
        print(".", end="", flush=True)
        time.sleep(15)

    raise TimeoutError(
        f"ComfyUI at {comfyui_url} did not respond within "
        f"{COMFYUI_READY_TIMEOUT // 60} minutes."
    )


# ── .env Patching ────────────────────────────────────────────────────────────

def patch_env_comfyui_url(comfyui_url: str) -> None:
    """Rewrite COMFYUI_URL in youtube_bot/.env without touching other keys."""
    text = ENV_PATH.read_text(encoding="utf-8")

    if re.search(r"^COMFYUI_URL=", text, flags=re.MULTILINE):
        text = re.sub(
            r"^COMFYUI_URL=.*$",
            f"COMFYUI_URL={comfyui_url}",
            text,
            flags=re.MULTILINE,
        )
    else:
        text = text.rstrip() + f"\nCOMFYUI_URL={comfyui_url}\n"

    ENV_PATH.write_text(text, encoding="utf-8")
    os.environ["COMFYUI_URL"] = comfyui_url
    print(f"[ENV] COMFYUI_URL set → {comfyui_url}")


# ── Local Pipeline ───────────────────────────────────────────────────────────

def run_local_pipeline(topic: str, no_upload: bool, shorts: bool) -> int:
    """Run main.py as a local subprocess inside youtube_bot/."""
    cmd = [sys.executable, "main.py", topic]
    if no_upload:
        cmd.append("--no-upload")
    if shorts:
        cmd.append("--shorts")

    print(f"\n[PIPELINE] Running: {' '.join(cmd)}")
    print("[PIPELINE] " + "=" * 56)

    result = subprocess.run(cmd, cwd=str(BOT_DIR))
    return result.returncode


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="runpod_launch.py",
        description=(
            "Spin up a RunPod ComfyUI pod, auto-download models, "
            "generate a video, then terminate the pod."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python runpod_launch.py "Europa's Hidden Ocean"
  python runpod_launch.py "The History of Rome" --no-upload
  python runpod_launch.py "Mars Colonization" --shorts
        """,
    )
    parser.add_argument("topic", help="Video topic / title to generate")
    parser.add_argument(
        "--no-upload",
        action="store_true",
        help="Skip YouTube upload (video saved locally)",
    )
    parser.add_argument(
        "--shorts",
        action="store_true",
        help="Also generate YouTube Shorts after main video",
    )
    args = parser.parse_args()

    # Validate config
    if not RUNPOD_API_KEY:
        print("[ERROR] RUNPOD_API_KEY not found in youtube_bot/.env")
        print("        Add: RUNPOD_API_KEY=your_key_here")
        sys.exit(1)

    runpod.api_key = RUNPOD_API_KEY

    pod_id: str | None = None
    pipeline_exit_code = 1

    print("\n" + "=" * 60)
    print(f"  RunPod ComfyUI Automation")
    print(f"  Topic: {args.topic[:56]}")
    print("=" * 60)

    try:
        # Step 1 — Find GPU
        gpu_name, gpu_id = find_available_gpu()

        # Step 2 — Create pod
        pod_id = create_pod(gpu_id, gpu_name)

        # Step 3 — Wait for RUNNING
        pod = wait_pod_running(pod_id)

        # Step 4 — SSH setup (clone, models, FastAPI)
        setup_pod_via_ssh(pod, pod_id)

        # Step 5 — Wait for ComfyUI to load models
        comfyui_url = get_proxy_url(pod_id, COMFYUI_PORT)
        wait_comfyui_ready(comfyui_url)

        # Step 6 — Patch local .env
        patch_env_comfyui_url(comfyui_url)

        # Step 7 — Run pipeline locally
        pipeline_exit_code = run_local_pipeline(args.topic, args.no_upload, args.shorts)

        if pipeline_exit_code == 0:
            print("\n[OK] Pipeline completed successfully!")
        else:
            print(f"\n[✗] Pipeline exited with code {pipeline_exit_code}")

    except KeyboardInterrupt:
        print("\n\n[INTERRUPT] Ctrl+C — cleaning up pod...")
    except Exception as exc:
        print(f"\n[ERROR] {exc}")
    finally:
        # ALWAYS terminate pod — never leave it running
        if pod_id:
            terminate_pod(pod_id)

    sys.exit(pipeline_exit_code)


if __name__ == "__main__":
    main()
