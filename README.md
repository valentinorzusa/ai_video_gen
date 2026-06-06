# 🎬 AI Video Generator

An automated pipeline that generates full-length (up to 20 minutes) YouTube escapism documentaries from a single topic. It writes the script, generates the voiceover, creates/downloads the video clips, edits everything together with background music, and uploads it to YouTube as a private video for review.

## 🚀 How to Use

### 1. Prerequisites
- Python 3.10+
- `ffmpeg` installed and available in your system's PATH.

### 2. Installation

1. Clone this repository and enter the `youtube_bot` directory:
   ```bash
   git clone https://github.com/valentinorzusa/ai_video_gen.git
   cd ai_video_gen/youtube_bot
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuration

1. **Environment Variables**: Copy the example configuration file:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and fill in your API keys (Gemini, ElevenLabs, etc.) and your RunPod ComfyUI URL.

2. **YouTube Credentials**: Place your YouTube OAuth 2.0 Client Secrets JSON file in the `youtube_bot` folder and name it `client_secret.json`.

3. **Background Music**: Place ambient `.mp3` or `.wav` files inside the `youtube_bot/music/` directory. These will be looped and played at a low volume under the voiceover.

### 4. Running the Bot

Run the main script with the topic you want a documentary about.

**Run the full pipeline (including YouTube upload):**
```bash
python main.py "Europa's Hidden Ocean"
```

**Run the pipeline locally (skip YouTube upload):**
```bash
python main.py "The History of Rome" --no-upload
```

## 🧠 How It Works (The Pipeline)

The generation process consists of 5 sequential steps:
1. **The Writer (`01_brain.py`)**: Uses LLMs (Gemini/Anthropic) to write a script with a narrative arc and splits it into scenes. Output: `data.json`
2. **The Voice Actor (`02_voice.py`)**: Uses ElevenLabs to generate a realistic voiceover for the entire script. Output: `voiceover.mp3`
3. **The Scout (`03_vision.py`)**: Generates custom video using ComfyUI (LTXV model) and downloads stock footage using Pexels. Output: `clips/*.mp4`
4. **The Editor (`04_composer.py`)**: Uses MoviePy to stitch the voiceover, video clips, and background music together. Output: `final_render.mp4`
5. **The Distributor (`05_publisher.py`)**: Authenticates with the YouTube API and uploads the final video as a private draft.

*For deep technical details on the architecture and known issues, see [WALKTHROUGH.md](youtube_bot/WALKTHROUGH.md).*
