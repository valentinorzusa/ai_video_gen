# 🎬 AI Video Generator — Walkthrough

## Overview

Automated pipeline that generates 20-minute YouTube escapism documentaries. Five scripts execute sequentially, each producing an artifact consumed by the next.

---

## Pipeline Flow

```mermaid
flowchart TD
    A["🧠 01_brain.py\n(The Writer)"] -->|data.json| B["🎙️ 02_voice.py\n(The Voice Actor)"]
    A -->|data.json| C["👁️ 03_vision.py\n(The Scout)"]
    B -->|voiceover.mp3| D["🎬 04_composer.py\n(The Editor)"]
    C -->|clips/*.mp4| D
    D -->|final_render.mp4| E["📤 05_publisher.py\n(The Distributor)"]
    A -->|data.json| E

    style A fill:#7c3aed,color:#fff
    style B fill:#2563eb,color:#fff
    style C fill:#059669,color:#fff
    style D fill:#d97706,color:#fff
    style E fill:#dc2626,color:#fff
```

---

## Data Flow & Artifacts

```mermaid
flowchart LR
    subgraph Inputs
        T["Topic string"]
        ENV[".env (API keys)"]
        MUS["music/*.mp3"]
    end

    subgraph Pipeline
        BRAIN["01_brain"]
        VOICE["02_voice"]
        VISION["03_vision"]
        COMP["04_composer"]
        PUB["05_publisher"]
    end

    subgraph Artifacts
        DJ["data.json"]
        VO["voiceover.mp3"]
        CL["clips/*.mp4"]
        FR["final_render.mp4"]
    end

    T --> BRAIN
    ENV --> BRAIN & VOICE & VISION & PUB
    BRAIN --> DJ
    DJ --> VOICE & VISION & PUB
    VOICE --> VO
    VISION --> CL
    VO & CL & MUS --> COMP
    COMP --> FR
    FR --> PUB
```

---

## Step-by-Step Breakdown

### Step 1 — `01_brain.py` (The Writer)

```mermaid
sequenceDiagram
    participant M as main.py
    participant B as 01_brain.py
    participant C as Claude API

    M->>B: generate_script(topic)
    B->>C: POST /messages (system prompt + topic)
    C-->>B: JSON response
    B->>B: Parse + validate JSON
    B->>B: Write data.json
    B-->>M: return data dict
```

**Input:** Topic string (e.g., `"Europa's Hidden Ocean"`)

**Output:** `output/data.json`
```json
{
  "title": "...",
  "description": "...",
  "tags": ["space", "europa", "..."],
  "synthetic_content_label": true,
  "blocks": [
    {
      "block_id": 1,
      "voiceover": "Narration text...",
      "visual_prompt": "Visual description...",
      "visual_type": "stock | ai_generated",
      "duration_hint_sec": 15
    }
  ]
}
```

**Key:** System prompt enforces YouTube compliance (no clickbait, narrative arc, scientific rigor).

---

### Step 2 — `02_voice.py` (The Voice Actor)

```mermaid
sequenceDiagram
    participant M as main.py
    participant V as 02_voice.py
    participant E as ElevenLabs API
    participant F as ffmpeg

    M->>V: generate_voiceover()
    V->>V: Read data.json → combine all voiceover text
    V->>V: Split text at sentence boundaries (5000 char limit)
    loop Each chunk
        V->>E: POST /text-to-speech/{voice_id}
        E-->>V: MP3 audio bytes
        V->>V: Save chunk_NNN.mp3
    end
    V->>F: Concatenate all chunks
    F-->>V: voiceover.mp3
    V-->>M: return path
```

**Input:** `data.json`

**Output:** `output/voiceover.mp3`

**Key:** ElevenLabs has ~5000 char/request limit → text split at sentence boundaries → chunks concatenated via ffmpeg.

---

### Step 3 — `03_vision.py` (The Scout/Generator)

```mermaid
flowchart TD
    START["Read data.json blocks"] --> LOOP{"For each block"}
    LOOP --> CHECK{"visual_type?"}
    CHECK -->|stock| PEXELS["Pexels API\n(free B-Roll)"]
    CHECK -->|ai_generated| AI["Runway/Luma API\n(high-impact)"]
    AI -->|not yet implemented| FALLBACK["Fallback → Pexels"]
    PEXELS --> DL["Download .mp4"]
    FALLBACK --> DL
    DL --> SAVE["Save clip_NNN.mp4"]
    SAVE --> LOOP
    LOOP -->|done| OUT["output/clips/"]

    style PEXELS fill:#059669,color:#fff
    style AI fill:#7c3aed,color:#fff
    style FALLBACK fill:#d97706,color:#fff
```

**Input:** `data.json`

**Output:** `output/clips/clip_001.mp4`, `clip_002.mp4`, ...

**Key:** Hybrid sourcing → stock for general context (galaxies, labs), AI only for high-impact moments. Cuts cost ~70%.

---

### Step 4 — `04_composer.py` (The Editor)

```mermaid
flowchart TD
    VO["voiceover.mp3"] --> DUR["Calculate duration"]
    CL["clips/*.mp4"] --> LOOP["Loop clips to match duration"]
    DUR --> LOOP
    LOOP --> VID["Concatenated video track"]
    MUS["music/*.mp3"] --> MUSIC["Loop + set volume 10%"]
    VO --> MIX["CompositeAudioClip"]
    MUSIC --> MIX
    VID --> FINAL["Set audio on video"]
    MIX --> FINAL
    FINAL --> RENDER["Write final_render.mp4\n(libx264 + AAC, 24fps)"]

    style RENDER fill:#d97706,color:#fff
```

**Input:** `voiceover.mp3` + `clips/*.mp4` + `music/*.mp3`

**Output:** `output/final_render.mp4`

**Key:** MoviePy sequences clips, loops if not enough to fill voiceover duration. Background music at 10% volume.

---

### Step 5 — `05_publisher.py` (The Distributor)

```mermaid
sequenceDiagram
    participant M as main.py
    participant P as 05_publisher.py
    participant Y as YouTube API v3

    M->>P: upload_video()
    P->>P: Read data.json (title, desc, tags)
    P->>P: OAuth2 authentication
    P->>Y: videos.insert (resumable upload, 10MB chunks)
    loop Upload chunks
        Y-->>P: progress %
    end
    Y-->>P: video_id
    P-->>M: return video_id
```

**Input:** `final_render.mp4` + `data.json`

**Output:** Video uploaded to YouTube (private by default)

**Key:** Uploads as **private** → manual review before public. Console reminder to mark "Synthetic Content" in YouTube Studio.

---

## Running the Pipeline

```bash
# 1. Setup
cd youtube_bot
cp .env.example .env     # fill API keys
pip install -r requirements.txt

# 2. Drop ambient music
#    Place .mp3/.wav files in music/

# 3. Run (without upload)
python main.py "Europa's Hidden Ocean" --no-upload

# 4. Run (full pipeline with upload)
python main.py "Europa's Hidden Ocean"
```

---

## Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| Sequential execution | Each step depends on previous output |
| `importlib` in main.py | Numeric-prefixed filenames can't be imported normally |
| Sentence-boundary chunking | Avoids cutting words mid-sentence for TTS |
| Hybrid video sourcing | AI video only where needed → 70% cost reduction |
| Local music library | Avoids Content ID strikes vs AI-generated music |
| Private upload default | Human review before public — YouTube compliance |
| `data.json` as central artifact | Single source of truth for metadata across all steps |

---

## Known Issues & Fixes

### ⏱️ Video Duration Too Short (8 min instead of 20 min)

**Root cause:** `01_brain.py` system prompt said "20 minutes" but gave no enforceable word/block constraints. LLM generated ~15-20 blocks × short voiceovers → ~8 min.

**Fix (implemented — see spec.md §6):**

```mermaid
flowchart TD
    GEN["Gemini generates script"] --> COUNT["Count total words"]
    COUNT --> CHECK{"words ≥ 2700?"}
    CHECK -->|yes| SAVE["Save data.json"]
    CHECK -->|no| RETRY{"retries < 2?"}
    RETRY -->|yes| FEEDBACK["Send feedback prompt:\n'Too short, need more blocks'"] --> GEN
    RETRY -->|no| WARN["⚠ Log warning, save anyway"]

    style CHECK fill:#059669,color:#fff
    style RETRY fill:#d97706,color:#fff
    style WARN fill:#dc2626,color:#fff
```

**Changes required:**

| File | Change |
|------|--------|
| `config.py` | Add `TARGET_NARRATION_WORDS=3000`, `MIN_NARRATION_WORDS=2700`, `MAX_BRAIN_RETRIES=2` |
| `01_brain.py` | Rewrite system prompt: explicit word budget (3000-3200 words, 60-80 blocks, 40-50 words/block) + narrative structure skeleton (Hook/Act1/Act2/Act3/Outro) |
| `01_brain.py` | Add validation loop: count words → retry if < 2700 → max 2 retries |
| `01_brain.py` | Add post-gen stats: block count, word count, estimated duration |

## 7. Model Architecture & Workflow JSON Rewiring

**Root cause:** The user's original `47d245c34a7d.json` workflow was designed for the leaked/unreleased `ltx-2.3-22b` which featured **native audio generation** and used a **Gemma 3 text encoder**. However, the officially released public model is `ltxv-13b-0.9.8`, which is **video-only** and uses a **T5-XXL text encoder**. 
This caused a cascade of workflow crashes when `03_vision.py` submitted jobs to ComfyUI:
1. `AttributeError: 'Linear' object has no attribute 'weight'` when the custom nodes (`TextGenerateLTX2Prompt` and `LTXAVTextEncoderLoader`) attempted to load the `fp4_mixed` Gemma 3 models.
2. `Audio VAE config is required` when `LTXVAudioVAELoader` attempted to load audio configurations from the video-only `ltxv-13b` model.

**Fix (implemented):**
1. **Removed Audio Generation:** Stripped out `LTXVAudioVAELoader`, `LTXVAudioVAEDecode`, `LTXVEmptyLatentAudio`, and the A/V Latent Concatenation/Separation nodes entirely. Rewired the `video_latent` directly from the video sampler to the VAE Decoder and upsampler.
2. **Replaced Text Encoder:** Replaced the proprietary `LTXAVTextEncoderLoader` with the standard ComfyUI `CLIPLoader` node, configured to load the `t5xxl_fp8_e4m3fn.safetensors` model specifically for the `ltxv` architecture type.
3. **Bypassed Auto-Enhancer:** Removed the buggy `TextGenerateLTX2Prompt` node which crashed on FP4 weights, routing the Gemini prompt directly into the standard `CLIPTextEncode` node.
4. **Corrected Prompt Injection:** Updated `.env` to set `COMFYUI_PROMPT_NODE=267:266` so that `03_vision.py` correctly injects the unique prompt for each clip, instead of reusing the default placeholder.
5. **Fixed Path Placement:** Moved the `ltxv-spatial-upscaler-0.9.8.safetensors` from `models/upscale_models` to `models/latent_upscale_models` where the `LatentUpscaleModelLoader` node expects it.

The pipeline successfully submits and polls ComfyUI without errors, correctly generating text-to-video for each block using `LTXV-13B`.
