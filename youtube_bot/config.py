"""
Central configuration -- all API keys, paths, and constants.
Loads from .env file via python-dotenv.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# -- Paths --
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = OUTPUT_DIR / "temp"
CLIPS_DIR = OUTPUT_DIR / "clips"
MUSIC_DIR = BASE_DIR / "music"
DATA_JSON = OUTPUT_DIR / "data.json"
VOICEOVER_PATH = OUTPUT_DIR / "voiceover.mp3"
FINAL_RENDER = OUTPUT_DIR / "final_render.mp4"

# Resources (shared across project)
RESOURCES_DIR = BASE_DIR.parent / "resources"
SONGS_DIR = RESOURCES_DIR / "songs"
FONT_PATH = RESOURCES_DIR / "KOMIKAX_.ttf"

# Create dirs on import
for d in [OUTPUT_DIR, TEMP_DIR, CLIPS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# -- API Keys --
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")  # optional fallback

# -- ComfyUI (RunPod remote GPU) --
# Set to your RunPod proxy URL, e.g. https://abc123-8188.proxy.runpod.net
COMFYUI_URL = os.getenv("COMFYUI_URL", "").rstrip("/")
COMFYUI_WORKFLOW = os.getenv("COMFYUI_WORKFLOW", "comfyui_workflow.json")
COMFYUI_PROMPT_NODE = os.getenv("COMFYUI_PROMPT_NODE", "340:319")
COMFYUI_TIMEOUT = int(os.getenv("COMFYUI_TIMEOUT", "600"))  # seconds per clip
COMFYUI_VIDEO_FRAMES = int(os.getenv("COMFYUI_VIDEO_FRAMES", "81"))  # ~5s @ 16fps
COMFYUI_VIDEO_FPS = int(os.getenv("COMFYUI_VIDEO_FPS", "16"))
COMFYUI_VIDEO_STEPS = int(os.getenv("COMFYUI_VIDEO_STEPS", "20"))

# -- YouTube --
YOUTUBE_ACCOUNT_FILE = BASE_DIR / "youtube_account.yaml"
YOUTUBE_CLIENT_SECRETS = os.getenv("YOUTUBE_CLIENT_SECRETS", "client_secret.json")

# -- ElevenLabs --
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "TxGEqnHWrfWFTfGW9XjX")  # Josh
ELEVENLABS_MODEL = "eleven_turbo_v2_5"
ELEVENLABS_CHUNK_LIMIT = 5000  # chars per TTS request

# -- Video Generation --
TARGET_VIDEO_DURATION_MIN = 9
CLIP_DURATION_SEC = 5  # avg clip length

# -- Audio Mixing (LUFS-compliant) --
VOICEOVER_TARGET_LUFS = -16     # YouTube integrated loudness standard
MUSIC_TARGET_LUFS = -30         # background music well below voice
MUSIC_CROSSFADE_SEC = 3.0       # crossfade overlap between tracks
END_FADE_DURATION = 2.0         # music fade-out after last voiceover word

# -- Vignette --
VIGNETTE_INTENSITY = "PI/4"     # ffmpeg vignette angle (PI/4 = moderate)

# -- Narration Duration Enforcement --
NARRATION_WPM = 150
TARGET_NARRATION_WORDS = 1350   # 150 wpm x 9 min
MIN_NARRATION_WORDS = 1200      # ~8 min floor
TARGET_BLOCKS = 30
MAX_BRAIN_RETRIES = 2

# -- Shorts Generation --
SHORTS_DIR = OUTPUT_DIR / "shorts"
SHORT_TARGET_DURATION = 30    # seconds per short
SHORT_MAX_DURATION = 58       # hard cap (YouTube max = 60)
SHORT_MIN_DURATION = 20       # skip segments shorter than this
