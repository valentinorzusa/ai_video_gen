"""
05_publisher.py -- The Distributor
Uses YouTube Data API v3 to upload final_render.mp4.
Loads settings from youtube_account.yaml.
Auto-detects category (Science & Tech vs Education/History).
Sets metadata from data.json. Marks altered/synthetic content.
Supports --preview flag (forces private upload).
"""
import json
import yaml

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pathlib import Path

from config import DATA_JSON, FINAL_RENDER, YOUTUBE_ACCOUNT_FILE, YOUTUBE_CLIENT_SECRETS

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_FILE = Path(__file__).parent / "token.json"

# Category mapping
CATEGORIES = {
    "science": "28",     # Science & Technology
    "tech": "28",        # Science & Technology
    "technology": "28",  # Science & Technology
    "history": "27",     # Education
    "education": "27",   # Education
}


def _load_youtube_config() -> dict:
    """Load youtube_account.yaml settings."""
    if YOUTUBE_ACCOUNT_FILE.exists():
        with open(YOUTUBE_ACCOUNT_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def _detect_category(data: dict) -> str:
    """Auto-detect YouTube category from video title/description/tags.
    Returns category ID: '28' (Science & Tech) or '27' (Education/History).
    """
    text = " ".join([
        data.get("title", ""),
        data.get("description", ""),
        " ".join(data.get("tags", [])),
    ]).lower()

    # Check for history keywords
    history_keywords = ["history", "ancient", "historical", "civilization", "empire",
                        "war", "century", "medieval", "dynasty", "archaeological"]
    history_score = sum(1 for kw in history_keywords if kw in text)

    # Check for science/tech keywords
    science_keywords = ["space", "telescope", "planet", "galaxy", "nasa", "science",
                        "physics", "quantum", "atom", "molecule", "technology", "ai",
                        "cosmic", "universe", "star", "dark matter", "exoplanet"]
    science_score = sum(1 for kw in science_keywords if kw in text)

    if history_score > science_score:
        return "27"  # Education (History)
    return "28"      # Science & Technology (default)


def _get_authenticated_service():
    """Authenticate via OAuth2 -> YouTube service."""
    from config import BASE_DIR
    config = _load_youtube_config()
    secrets_file = config.get("client_secrets_file", YOUTUBE_CLIENT_SECRETS)

    # Make secrets_file absolute relative to BASE_DIR (youtube_bot dir)
    secrets_path = Path(secrets_file)
    if not secrets_path.is_absolute():
        # Handle cases where user typed "youtube_bot/client_secret.json"
        if secrets_path.parts[0] == "youtube_bot":
            secrets_path = Path(*secrets_path.parts[1:])
        secrets_path = BASE_DIR / secrets_path

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(secrets_path), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())

    return build("youtube", "v3", credentials=creds)


def upload_video(preview: bool = False) -> str:
    """Upload final_render.mp4 with auto-filled metadata.

    Args:
        preview: If True, upload as private (for testing). Otherwise uses config.
    """
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    config = _load_youtube_config()
    youtube = _get_authenticated_service()

    # -- Build metadata --
    title = data.get("title", "Untitled Documentary")

    # Description: video description + config footer
    description = data.get("description", "")
    footer = config.get("description_footer", "")
    if footer:
        description += "\n" + footer.strip()
    # Always add synthetic content notice
    if "synthetic" not in description.lower() and "ai-generated" not in description.lower():
        description += "\n\nThis video contains AI-generated synthetic visuals."

    # Tags: merge video tags + config default_tags
    tags = list(data.get("tags", []))
    default_tags = config.get("default_tags", [])
    for tag in default_tags:
        if tag not in tags:
            tags.append(tag)

    # Category: auto-detect
    category_id = _detect_category(data)
    category_name = "Education/History" if category_id == "27" else "Science & Technology"
    print(f"[PUBLISHER] Category auto-detected: {category_name} ({category_id})")

    # Privacy
    if preview:
        privacy = "private"
        print("[PUBLISHER] PREVIEW MODE: uploading as PRIVATE")
    else:
        privacy = config.get("privacy_status", "public")

    # Language
    language = config.get("default_language", "en")

    body = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "tags": tags[:500],
            "categoryId": category_id,
            "defaultLanguage": language,
            "defaultAudioLanguage": language,
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": config.get("made_for_kids", False),
        },
    }

    media = MediaFileUpload(
        str(FINAL_RENDER),
        mimetype="video/mp4",
        resumable=True,
        chunksize=10 * 1024 * 1024,
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    print(f"[PUBLISHER] Uploading: {title[:60]}...")
    print(f"[PUBLISHER] Privacy: {privacy}")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"[PUBLISHER]   {pct}% uploaded")

    video_id = response["id"]
    video_url = f"https://youtube.com/watch?v={video_id}"
    print(f"[PUBLISHER] [OK] Uploaded -> {video_url}")
    print(f"[PUBLISHER] [!] Mark 'Altered/Synthetic Content' in YouTube Studio")

    return video_id


if __name__ == "__main__":
    import sys
    preview = "--preview" in sys.argv
    upload_video(preview=preview)
