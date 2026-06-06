"""
01_brain.py — The Writer
Generates script in 3 sections (chunked) to ensure reliable JSON parsing.
Each section produces ~20 blocks → small JSON → no truncation/corruption.
Merges sections into final data.json.

Duration enforcement: targets 3000+ words across ~65 blocks.
"""
import json
import re
import time
from google import genai
from google.genai import errors as genai_errors
from config import (
    GEMINI_API_KEY,
    DATA_JSON,
    MAX_BRAIN_RETRIES,
    MIN_NARRATION_WORDS,
    NARRATION_WPM,
    TARGET_NARRATION_WORDS,
    TARGET_BLOCKS,
)

# Max retries specifically for transient server errors (503/429/500)
MAX_SERVER_RETRIES = 4
SERVER_RETRY_BASE_DELAY = 5  # seconds, doubles each retry: 5→10→20→40

COMPLIANCE_RULES = """You are the content director for an automated YouTube channel specialized in escapism documentaries.

COMPLIANCE RULES:
1. REPETITIVE CONTENT: Every script must have a narrative arc (Hook/Conflict/Resolution), unique tone, curated perspective. No Wikipedia readings.
2. SYNTHETIC CONTENT: Include synthetic_content_label: true. Avoid hyper-realistic human faces of real people.
3. MISINFORMATION: Scientific rigor. Conditional language ("scientists believe"). No misleading clickbait.
4. COPYRIGHT: B-Roll changes every 4-7 seconds. Voiceover always provides educational context.

BLOCK FORMAT — each block in the "blocks" array:
{
  "block_id": N,
  "voiceover": "40-55 words of narration text...",
  "visual_prompt": "What the visual should show...",
  "pexels_query": "1-3 broad search words",
  "visual_type": "stock",
  "duration_hint_sec": 15
}

visual_type must be exactly the string "stock" or "ai_generated".
Use "ai_generated" ONLY for high-impact moments (alien landscapes, extinct creatures, deep ocean).
Use "stock" for general context (galaxies, scientists, labs, rockets).
Each block voiceover MUST be 40-55 words. This is critical for hitting the 9-minute target duration.
"""


def _count_words(data: dict) -> int:
    """Count total words across all voiceover fields."""
    return sum(len(b["voiceover"].split()) for b in data.get("blocks", []))


def _parse_response(raw: str) -> dict:
    """Parse LLM response → dict. Handles fences, trailing commas, enum expressions."""
    raw = raw.strip()

    # Strip markdown fences
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```\s*$", "", raw)

    # Direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Brace-matching extraction
    for open_ch, close_ch in [("{", "}"), ("[", "]")]:
        start = raw.find(open_ch)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(raw)):
            if raw[i] == open_ch:
                depth += 1
            elif raw[i] == close_ch:
                depth -= 1
                if depth == 0:
                    extracted = raw[start:i + 1]
                    # Fix common LLM JSON errors
                    fixed = re.sub(r",\s*([}\]])", r"\1", extracted)
                    fixed = re.sub(r'"stock"\s*\|\s*"ai_generated"', '"stock"', fixed)
                    try:
                        return json.loads(fixed)
                    except json.JSONDecodeError:
                        break

    raise ValueError("No valid JSON found in response")


def _call_gemini_once(client, prompt: str) -> str:
    """Single Gemini API call with server-error retry + exponential backoff."""
    for server_attempt in range(MAX_SERVER_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    system_instruction=COMPLIANCE_RULES,
                    response_mime_type="application/json",
                    max_output_tokens=8192,
                ),
            )
            return response.text
        except (genai_errors.ServerError, genai_errors.APIError) as e:
            status = getattr(e, 'status_code', 0) or 0
            if status in (429, 500, 503) and server_attempt < MAX_SERVER_RETRIES:
                delay = SERVER_RETRY_BASE_DELAY * (2 ** server_attempt)
                print(f"[BRAIN]   ! Server {status} (attempt {server_attempt + 1}/{MAX_SERVER_RETRIES + 1}), retrying in {delay}s...")
                time.sleep(delay)
            else:
                raise


def _call_gemini(client, prompt: str, label: str = "") -> dict:
    """Call Gemini with retries on parse failure. Dumps raw response on final failure."""
    last_error = None
    raw_text = None
    for attempt in range(MAX_BRAIN_RETRIES + 1):
        try:
            raw_text = _call_gemini_once(client, prompt)
            return _parse_response(raw_text)
        except (json.JSONDecodeError, ValueError) as e:
            last_error = e
            print(f"[BRAIN]   ! {label} parse error (try {attempt + 1}): {e}")
            if attempt == MAX_BRAIN_RETRIES:
                dump_path = DATA_JSON.parent / f"debug_{label}.txt"
                if raw_text:
                    dump_path.write_text(raw_text, encoding="utf-8")
                    print(f"[BRAIN]   Raw response dumped -> {dump_path}")
                raise RuntimeError(f"{label} failed after {MAX_BRAIN_RETRIES + 1} tries: {last_error}")


def generate_script(topic: str) -> dict:
    """Generate script in 3 chunked sections for reliable JSON + 9-min duration."""
    client = genai.Client(api_key=GEMINI_API_KEY)

    # ── Section 1: Metadata + HOOK + ACT 1 (blocks 1-10, ~480 words) ──
    print("[BRAIN] Section 1/3: Metadata + Hook + Act 1...")
    s1_prompt = (
        f"Create the FIRST section of a 9-minute YouTube documentary about: {topic}\n\n"
        "Generate:\n"
        "1. Metadata: title, description, tags array, synthetic_content_label (true)\n"
        "2. Blocks 1 through 10:\n"
        "   - HOOK (blocks 1-3): Attention-grabbing opening + thesis\n"
        "   - ACT 1 (blocks 4-10): Context, background, historical setup\n\n"
        "Each block voiceover MUST be 40-55 words. "
        "Total voiceover across these 10 blocks should be ~450-500 words.\n\n"
        "Output as JSON with keys: title, description, tags, synthetic_content_label, blocks"
    )
    section1 = _call_gemini(client, s1_prompt, "section1")
    s1_words = _count_words(section1)
    s1_blocks = len(section1.get("blocks", []))
    print(f"[BRAIN]   ✓ {s1_blocks} blocks, {s1_words} words")

    # ── Section 2: ACT 2 (blocks 11-22, ~576 words) ──
    print("[BRAIN] Section 2/3: Act 2 (deep exploration)...")
    last_vo = section1["blocks"][-1]["voiceover"] if section1.get("blocks") else ""
    s2_prompt = (
        f"Continue the YouTube documentary about: {topic}\n"
        f"Title: {section1.get('title', '')}\n\n"
        f"The previous section ended with this narration:\n\"{last_vo}\"\n\n"
        "Now generate ACT 2 — the deep exploration core of the documentary.\n"
        "Generate blocks 11 through 22 (12 blocks).\n"
        "This section covers: conflict, mystery, deep science, key revelations, expert perspectives.\n\n"
        "Each block voiceover MUST be 40-55 words. "
        "Total voiceover across these 12 blocks should be ~550-650 words.\n\n"
        "Output as JSON with key: blocks (array of block objects)"
    )
    section2 = _call_gemini(client, s2_prompt, "section2")
    s2_words = _count_words(section2)
    s2_blocks = len(section2.get("blocks", []))
    print(f"[BRAIN]   ✓ {s2_blocks} blocks, {s2_words} words")

    # ── Section 3: ACT 3 + OUTRO (blocks 23-30, ~384 words) ──
    print("[BRAIN] Section 3/3: Act 3 + Outro...")
    last_vo = section2["blocks"][-1]["voiceover"] if section2.get("blocks") else ""
    s3_prompt = (
        f"Conclude the YouTube documentary about: {topic}\n"
        f"Title: {section1.get('title', '')}\n\n"
        f"The previous section ended with this narration:\n\"{last_vo}\"\n\n"
        "Generate the final section:\n"
        "- ACT 3 (blocks 23-28): Resolution, new perspective, implications\n"
        "- OUTRO (blocks 29): Summary, reflection\n"
        "- FINAL BLOCK (block 30): MUST be a call-to-action. "
        "The voiceover MUST end with words encouraging viewers to "
        "subscribe, leave a comment, and like the video. "
        "Example ending: '...subscribe and share your thoughts in the comments below.'\n\n"
        "Generate blocks 23 through 30 (8 blocks).\n"
        "Each block voiceover MUST be 40-55 words. "
        "Total voiceover across these 8 blocks should be ~350-450 words.\n\n"
        "CRITICAL: The very last block (block 30) voiceover MUST end with a "
        "subscribe/comment/like call-to-action. This is non-negotiable.\n\n"
        "Output as JSON with key: blocks (array of block objects)"
    )
    section3 = _call_gemini(client, s3_prompt, "section3")
    s3_words = _count_words(section3)
    s3_blocks = len(section3.get("blocks", []))
    print(f"[BRAIN]   ✓ {s3_blocks} blocks, {s3_words} words")

    # ── Merge all sections ──
    data = {
        "title": section1.get("title", topic),
        "description": section1.get("description", ""),
        "tags": section1.get("tags", []),
        "synthetic_content_label": section1.get("synthetic_content_label", True),
        "blocks": [],
    }

    all_blocks = (
        section1.get("blocks", [])
        + section2.get("blocks", [])
        + section3.get("blocks", [])
    )

    # Re-number block_ids sequentially
    for i, block in enumerate(all_blocks, 1):
        block["block_id"] = i
        data["blocks"].append(block)

    total_words = _count_words(data)
    est_minutes = total_words / NARRATION_WPM

    if total_words < MIN_NARRATION_WORDS:
        print(
            f"[BRAIN] ⚠ Total {total_words} words (~{est_minutes:.1f} min) "
            f"— below {MIN_NARRATION_WORDS} target. Proceeding anyway."
        )

    # Persist
    DATA_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    block_count = len(data["blocks"])
    ai_blocks = sum(1 for b in data["blocks"] if b.get("visual_type") == "ai_generated")
    stock_blocks = block_count - ai_blocks

    print(f"[BRAIN] ✓ Script: {block_count} blocks, {total_words} words (~{est_minutes:.1f} min @ {NARRATION_WPM}wpm)")
    print(f"[BRAIN]   Breakdown: {ai_blocks} AI, {stock_blocks} stock")
    print(f"[BRAIN]   Title: {data['title']}")
    return data


if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else "The Hidden Ocean of Europa: Could Life Exist Beneath the Ice?"
    generate_script(topic)
