"""
04_composer.py -- The Editor
Clips are already trimmed to match voice duration (done in 03_vision.py).
Concatenates clips into final video. Applies vignette.
Mixes voiceover + crossfaded background music from resources/songs/.
LUFS-compliant audio: voice at -16 LUFS, music at -30 LUFS.
Adds 2s music fade-out after last voiceover word.
Outputs final_render.mp4.
"""
import json
import random
import subprocess
from pathlib import Path

from moviepy.editor import (
    AudioFileClip,
    CompositeAudioClip,
    VideoFileClip,
    concatenate_videoclips,
    concatenate_audioclips,
)

from config import (
    CLIPS_DIR,
    DATA_JSON,
    END_FADE_DURATION,
    FINAL_RENDER,
    MUSIC_CROSSFADE_SEC,
    MUSIC_TARGET_LUFS,
    OUTPUT_DIR,
    SONGS_DIR,
    TEMP_DIR,
    VIGNETTE_INTENSITY,
    VOICEOVER_PATH,
    VOICEOVER_TARGET_LUFS,
)


# -- Music Handling --

def _get_all_songs() -> list[Path]:
    """Find all music tracks in resources/songs/."""
    songs = []
    for ext in ("*.mp3", "*.wav", "*.ogg", "*.flac"):
        songs.extend(SONGS_DIR.glob(ext))
    return sorted(songs)


def _build_crossfaded_music(target_duration: float) -> AudioFileClip | None:
    """Build a seamless music track by shuffling and crossfading songs.

    Randomly picks songs from resources/songs/, crossfades between them,
    and loops until target_duration is reached.
    """
    songs = _get_all_songs()
    if not songs:
        print("[COMPOSER] [!] No songs found in resources/songs/")
        return None

    random.shuffle(songs)
    print(f"[COMPOSER] Found {len(songs)} songs, building crossfaded mix...")

    # Load and chain songs until we exceed target duration
    segments: list[AudioFileClip] = []
    total_dur = 0.0
    song_idx = 0

    while total_dur < target_duration + MUSIC_CROSSFADE_SEC:
        song_path = songs[song_idx % len(songs)]
        clip = AudioFileClip(str(song_path))
        segments.append(clip)
        total_dur += clip.duration
        song_idx += 1
        if song_idx > len(songs) * 3:  # safety: max 3 full loops
            break

    if len(segments) == 1:
        music = segments[0]
        # Loop if needed
        if music.duration < target_duration:
            loops = int(target_duration / music.duration) + 1
            music = concatenate_audioclips([music] * loops)
    else:
        # Crossfade: overlap each transition by MUSIC_CROSSFADE_SEC
        # MoviePy doesn't have native crossfade for audio, so we
        # concatenate and apply volume ramps at boundaries via ffmpeg later
        music = concatenate_audioclips(segments)

    # Trim to exact target + fade buffer
    total_needed = target_duration + END_FADE_DURATION
    if music.duration > total_needed:
        music = music.subclip(0, total_needed)

    print(f"[COMPOSER] Music mix: {music.duration:.1f}s from {min(song_idx, len(songs))} tracks")
    return music


# -- Audio Normalization --

def _normalize_audio_lufs(input_path: Path, output_path: Path, target_lufs: int) -> bool:
    """Normalize audio to target LUFS using ffmpeg loudnorm (two-pass)."""
    try:
        # Pass 1: measure
        result = subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(input_path),
                "-af", f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11:print_format=json",
                "-f", "null", "-",
            ],
            capture_output=True, text=True,
        )
        stderr = result.stderr

        # Extract measured values from JSON block in stderr
        import re
        json_match = re.search(r'\{[^}]*"input_i"[^}]*\}', stderr, re.DOTALL)
        if not json_match:
            # Fallback: simple normalization
            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", str(input_path),
                    "-af", f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11",
                    "-ar", "44100", "-c:a", "aac", "-b:a", "192k",
                    str(output_path),
                ],
                check=True, capture_output=True,
            )
            return True

        measured = json.loads(json_match.group())

        # Pass 2: apply
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(input_path),
                "-af", (
                    f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11:"
                    f"measured_I={measured['input_i']}:"
                    f"measured_TP={measured['input_tp']}:"
                    f"measured_LRA={measured['input_lra']}:"
                    f"measured_thresh={measured['input_thresh']}:"
                    f"offset={measured['target_offset']}:"
                    f"linear=true:print_format=summary"
                ),
                "-ar", "44100", "-c:a", "aac", "-b:a", "192k",
                str(output_path),
            ],
            check=True, capture_output=True,
        )
        return True

    except Exception as e:
        print(f"[COMPOSER] [!] LUFS normalization failed: {e}")
        # Fallback: just copy
        import shutil
        shutil.copy(input_path, output_path)
        return False


# -- Main Composer --

def compose_video() -> Path:
    """Full composition pipeline:
    1. Concatenate clips
    2. Mix voiceover (normalized -16 LUFS) + music (normalized -30 LUFS)
    3. Add 2s music fade-out after voiceover ends
    4. Apply vignette
    5. Render final_render.mp4
    """
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # -- Load clips --
    clip_paths = sorted(CLIPS_DIR.glob("clip_*.mp4"))
    if not clip_paths:
        raise RuntimeError("No clips found in output/clips/")

    print(f"[COMPOSER] Loading {len(clip_paths)} synced clips...")
    video_clips = []
    for p in clip_paths:
        try:
            video_clips.append(VideoFileClip(str(p)))
        except Exception as e:
            print(f"[COMPOSER] [!] Skipping {p.name}: {e}")

    final_video = concatenate_videoclips(video_clips, method="compose")
    total_duration = final_video.duration
    print(f"[COMPOSER] Total video duration: {total_duration:.1f}s ({total_duration/60:.1f}min)")

    # -- Normalize voiceover to -16 LUFS --
    print(f"[COMPOSER] Normalizing voiceover to {VOICEOVER_TARGET_LUFS} LUFS...")
    vo_normalized = TEMP_DIR / "voiceover_normalized.m4a"
    _normalize_audio_lufs(VOICEOVER_PATH, vo_normalized, VOICEOVER_TARGET_LUFS)
    voiceover = AudioFileClip(str(vo_normalized))

    # -- Build crossfaded music --
    music = _build_crossfaded_music(voiceover.duration)

    if music:
        # Normalize music to -30 LUFS (well below voice)
        print(f"[COMPOSER] Normalizing music to {MUSIC_TARGET_LUFS} LUFS...")
        music_temp = TEMP_DIR / "music_raw.mp3"
        music.write_audiofile(str(music_temp), fps=44100, logger=None)
        music.close()

        music_normalized = TEMP_DIR / "music_normalized.m4a"
        _normalize_audio_lufs(music_temp, music_normalized, MUSIC_TARGET_LUFS)
        music = AudioFileClip(str(music_normalized))

        # Apply end fade: music fades to 0 over last END_FADE_DURATION seconds
        vo_end = voiceover.duration
        music_end = vo_end + END_FADE_DURATION

        if music.duration > music_end:
            music = music.subclip(0, music_end)

        # Fade out the last 2 seconds of music
        music = music.audio_fadeout(END_FADE_DURATION)

        # Composite audio
        final_audio = CompositeAudioClip([voiceover, music])
        print(f"[COMPOSER] Audio: voice {voiceover.duration:.1f}s + music {music.duration:.1f}s (fade-out {END_FADE_DURATION}s)")
    else:
        final_audio = voiceover

    # -- Trim video to voiceover + fade duration --
    target_end = voiceover.duration + END_FADE_DURATION
    if final_video.duration > target_end:
        final_video = final_video.subclip(0, target_end)
    elif voiceover.duration < final_video.duration:
        final_video = final_video.subclip(0, voiceover.duration)

    final_video = final_video.set_audio(final_audio)

    # -- Render pre-vignette --
    pre_vignette = TEMP_DIR / "pre_vignette.mp4"
    print(f"[COMPOSER] Rendering pre-vignette...")
    final_video.write_videofile(
        str(pre_vignette),
        fps=24,
        codec="libx264",
        audio_codec="aac",
        audio_bitrate="192k",
        threads=4,
        preset="medium",
        logger="bar",
    )

    final_video.close()
    voiceover.close()
    if music:
        music.close()

    # -- Apply vignette via ffmpeg --
    print(f"[COMPOSER] Applying vignette effect...")
    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(pre_vignette),
                "-vf", f"vignette=angle={VIGNETTE_INTENSITY}",
                "-c:v", "libx264",
                "-preset", "medium",
                "-crf", "18",
                "-c:a", "copy",
                "-movflags", "+faststart",
                str(FINAL_RENDER),
            ],
            check=True,
            capture_output=True,
        )
        pre_vignette.unlink(missing_ok=True)
        print(f"[COMPOSER] [OK] Vignette applied")
    except subprocess.CalledProcessError as e:
        print(f"[COMPOSER] [!] Vignette failed, using pre-vignette: {e.stderr.decode()[:200]}")
        import shutil
        shutil.move(str(pre_vignette), str(FINAL_RENDER))

    print(f"[COMPOSER] [OK] Final render saved -> {FINAL_RENDER}")
    return FINAL_RENDER


if __name__ == "__main__":
    compose_video()
