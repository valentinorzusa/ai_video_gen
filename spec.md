# Long AI Video Generator for YouTube (20 min)

This tool will automate the creation of videos for YouTube.

The videos will be about:
**"Escapism" Documentaries and Science (Long-form)**
The main trend this year is content that allows the audience to disconnect from reality.

**Topics:** Space exploration, reconstruction of extinct species with AI, deep geography, and historical mysteries.

**Why they work:** People look for long videos (over 20 minutes) to watch on TVs (CTV) while relaxing. If you use AI to generate hyper-realistic visuals of ancient civilizations or distant planets, watch time skyrockets.

---

## 1. How are AI videos created?
There are different types of tools depending on what you need to automate:

* **Script generation:** Tools like ChatGPT or Claude can write full scripts, structure the key points of a video, and optimize titles for SEO.
* **Voiceover:** AIs like ElevenLabs or Speechelo generate highly realistic human voices from text, eliminating the need for a microphone or a professional voice actor.
* **Image and video generation:** 
  * To create clips from scratch, models like Runway, Luma Dream Machine, or Pika are used.
  * To edit "smart slide" or "storytelling" videos with stock footage, tools like InVideo or Pictory are used.
* **Digital Avatars:** Platforms like HeyGen or Synthesia allow you to create virtual presenters whose lips sync with the audio.

## 2. Does YouTube allow it?
Yes, YouTube allows AI-generated content, but it has implemented transparency rules:

* **Mandatory labeling:** If the video shows something that looks real but was created or altered with AI (especially real people, places, or events), you must check a box in the YouTube dashboard indicating that the "content is altered or synthetic."
* **Copyright:** You must ensure you have the rights to the images or music that the AI uses as a base. Most paid tools include commercial licenses.

## 3. Can they be monetized?
This is the most common question. The answer is yes, as long as the video provides original value:

* **Avoid repetitive content:** If you just let the AI do everything without human editing or a creative concept, YouTube might classify it as "low-quality" or "repetitive content" and deny monetization.
* **Human touch:** Ideally, you should use AI as a productivity tool (for researching, voiceovers, or generating clips) but maintain creative direction, editing, and a unique narrative.

## 4. Video Generation Automation Sequence & Architecture
*Orchestrated via **n8n local** (self-hosted workflow automation) delegating heavy processing to an asynchronous worker (FastAPI/Celery).*

The backend structure applies **Domain-Driven Design (DDD)** and **Hexagonal Architecture**. By completely decoupling the core logic (narrative and metadata) from external infrastructure (Runway/ElevenLabs APIs), the system implements robust retry logic. If an external API fails on clip 150, the 20-minute job recovers without failing.

1. **Script Generation**: Generate video script to last 20 min.
2. **Video Asset Sourcing (Hybrid)**: The worker classifies the script to optimize costs and reduce hallucination rates.
   - Use AI video APIs *only* for high-impact visual moments (e.g., diving into Europa's ocean).
   - Use Pexels or Pixabay APIs to pull free, safe B-Roll for general context (galaxies, scientists), cutting costs by 70%.
3. **Audio Design (Safe Monetization)**: To avoid Content ID risks and unpredictable AI generations (e.g., Suno), the orchestrator selects from a local catalog of royalty-free loops (ambient pads and space drones designed in FL Studio/Vital). It dynamically mixes the audio beneath the generated voiceover.
4. **Voiceover Generation**: Generate audio text from script.
5. **Watermark Management**: Instead of cropping the video height (which destroys the 16:9 aspect ratio and causes letterboxing), the custom FastAPI/Celery worker runs an FFmpeg pipeline to apply a slight, dynamic Gaussian blur exactly over the watermark's coordinates. Alternatively, run a local diffusion model (e.g., Stable Video Diffusion) to bypass source watermarks entirely.

## 5. Project Execution Pipeline
Main directory structure (e.g., `youtube_bot/`). `main.py` orchestrates execution order:

* **01_brain.py (The Writer):** Connects to Claude API with strict System Prompt. Outputs `data.json` (title, description, script array split by blocks of voiceover text + visual prompt).
* **02_voice.py (The Voice Actor):** Reads `data.json`. Sends text to ElevenLabs. Outputs `voiceover.mp3` in temp folder.
* **03_vision.py (The Scout/Generator):** Reads `data.json`. If block needs "generic B-Roll", pulls safe `.mp4` from free Pexels/Pixabay API. If "high-impact moment", calls Runway/Luma API. Outputs folder of numbered clips (`clip_01.mp4`, `clip_02.mp4`...).
* **04_composer.py (The Editor):** Uses Python MoviePy. Calculates `voiceover.mp3` duration. Sequentially joins video clips to match audio length. Adds local background music track at 10% volume. Outputs `final_render.mp4`.
* **05_publisher.py (The Distributor):** Uses YouTube Data API v3. Takes `final_render.mp4` and metadata from `data.json`. Uploads video with "Synthetic Content" label.


[SYSTEM PROMPT - YOUTUBE COMPLIANCE & MONETIZATION GUIDELINES]

You are the content director and Compliance Officer for an automated YouTube channel specialized in escapism documentaries (e.g., Space Exploration). Your goal is to generate scripts and video directives that strictly comply with YouTube Monetization Policies (YPP) and Community Guidelines.

When generating any content, you MUST apply the following unbreakable rules:

1. "REPETITIVE AND REUSED CONTENT" POLICY (CRITICAL FOR MONETIZATION)
- RULE: YouTube demonetizes automated channels if the content lacks "significant educational, narrative, or human value".
- ACTION: Never generate scripts that are simple readings of Wikipedia articles or lists of cold facts. Every script must have a clear narrative arc (Hook, Conflict/Mystery, Resolution), a unique author tone, and provide a curated perspective.

2. SYNTHETIC CONTENT POLICY (AI LABELING)
- RULE: YouTube requires creators to disclose if photorealistic content was altered or synthetically generated if it resembles a real event, place, or person.
- ACTION: When generating visual prompts (for B-Roll or clips), if you ask to recreate hyper-realistic cosmic events (e.g., the surface of Mars, NASA probes in action), you must include in the generated metadata the directive to check the "Synthetic Content" box when uploading the video. Avoid asking for hyper-realistic human faces of real people (deepfakes).

3. MISINFORMATION AND SPAM POLICY (ESPECIALLY IN SCIENCE/SPACE)
- RULE: Content cannot deliberately mislead users or present debunked conspiracy theories as actual facts.
- ACTION: Maintain scientific rigor. You can explore hypotheses (e.g., "there could be life under Europa's ice"), but never state them as confirmed facts if they are not. Use conditional language ("scientists believe", "theory suggests").
- METADATA: The titles and thumbnails you suggest must exactly match the content of the script. Zero misleading clickbait (e.g., do not suggest "NASA FINDS ALIENS" in the title if the video is about hypothetical microscopic bacteria).

4. COPYRIGHT POLICY (FAIR USE)
- RULE: The use of third-party material must be transformative.
- ACTION: If you suggest using real archival footage in the script (e.g., historical NASA clips), you must indicate that the B-Roll should change every 4-7 seconds and that the voiceover is always providing educational context about those images, to qualify under Fair Use laws.

EXPECTED OUTPUT:
Every time you generate a script, mentally verify this list. If the script or visual prompts cross any of these lines, rewrite the segment to prioritize the original narrative and scientific accuracy before delivering the response to the user.

Python version: 3.11

---

## 6. Duration Enforcement Plan (20-min target)

### Problem
`01_brain.py` asks Gemini for "20 minutes of narration" but provides no enforceable constraints. LLM generates ~15-20 blocks × ~25s speech each → ~8 min total. Target = 20 min (1200s).

### Root Cause Analysis
| Factor | Current | Required |
|--------|---------|----------|
| Word count guidance | None | ~3000 words (150 wpm × 20 min) |
| Block count | "unspecified" | ~60-80 blocks |
| Per-block length | "2-4 sentences" | ~40-50 words (~18-20s speech) |
| Validation | None | Check total words → retry if short |

### Implementation Plan

#### A. System Prompt Rewrite (`01_brain.py`)
- Remove vague "2-4 sentences" → replace w/ explicit word budget:
  - Total narration: **3000-3200 words** (maps to ~20 min at 150 wpm)
  - Block count: **60-80 blocks**
  - Per-block voiceover: **40-50 words** (~15-20s speech each)
- Add structural skeleton:
  - **Hook** (blocks 1-3): 2 min — attention grab + thesis
  - **Act 1** (blocks 4-20): 6 min — context, background, setup
  - **Act 2** (blocks 21-45): 8 min — deep exploration, conflict, mystery
  - **Act 3** (blocks 46-60): 3 min — resolution, perspective
  - **Outro** (blocks 61-65): 1 min — CTA, tease next video
- Add explicit instruction: "Count your words. Total voiceover text across all blocks MUST be 3000-3200 words."

#### B. Validation + Retry Loop (`01_brain.py`)
```python
MAX_RETRIES = 2
MIN_WORD_COUNT = 2700   # ~18 min floor
TARGET_WORD_COUNT = 3000
```
After LLM response:
1. Count total words across all `voiceover` fields
2. If `total_words < MIN_WORD_COUNT` → retry w/ feedback prompt:
   `"Script too short ({total_words} words, need {TARGET_WORD_COUNT}). Add more blocks with deeper narration."`
3. If still short after MAX_RETRIES → log warning, proceed (partial generation better than crash)

#### C. Config Constants (`config.py`)
Add:
```python
TARGET_NARRATION_WORDS = 3000
MIN_NARRATION_WORDS = 2700
TARGET_BLOCKS = 65
NARRATION_WPM = 150
MAX_BRAIN_RETRIES = 2
```

#### D. Post-Generation Stats (`01_brain.py`)
Print after generation:
```
[BRAIN] ✓ Script: 65 blocks, 3102 words (~20.7 min @ 150wpm)
```

### Verification
- Run `01_brain.py` w/ test topic → check word count ≥ 2700
- Run full pipeline → verify `voiceover.mp3` duration ≥ 18 min
- Check `final_render.mp4` duration ≥ 18 min