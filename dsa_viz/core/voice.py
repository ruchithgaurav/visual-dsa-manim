import asyncio
from pathlib import Path

import edge_tts


# ==========================================================
# Configuration
# ==========================================================

VOICE = "en-US-GuyNeural"
RATE = "+15%"
PITCH = "+0Hz"

AUDIO_ROOT = Path("assets/audio")
AUDIO_ROOT.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Internal Generator
# ==========================================================

async def _generate(text: str, filename: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=RATE,
        pitch=PITCH,
    )

    await communicate.save(filename)


# ==========================================================
# Public API
# ==========================================================

def generate(text: str, algorithm: str, index: int):
    """
    Generate narration only once.

    Folder Structure:
        assets/audio/
            Bubble_Sort/
                step_0.mp3
                step_1.mp3
                ...
    """

    algorithm_folder = algorithm.replace(" ", "_")

    folder = AUDIO_ROOT / algorithm_folder
    folder.mkdir(parents=True, exist_ok=True)

    filename = folder / f"step_{index}.mp3"

    if not filename.exists():
        print(f"[VOICE] Generating {filename.name}")
        asyncio.run(_generate(text, str(filename)))

    return str(filename)