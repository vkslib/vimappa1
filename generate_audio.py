#!/usr/bin/env python3
"""
Generate German audio files using edge-tts for A1 learners
"""
import asyncio
import edge_tts
import os
from pathlib import Path

# German voice (female, clear for learning)
VOICE = "de-DE-KatjaNeural"
# Slow rate for A1 learners (-20% speed)
RATE = "-20%"

# Updated audio data for all chapters (00-14)
audio_data = {
    "vocab": [
        ("Kapitel 0: Willkommen!", "chapter00_vocab.mp3"),
        ("Kapitel 1: Erste Schritte.", "chapter01_vocab.mp3"),
        # Add entries for chapters 2-14 here
        ("wünschen", "unit13_wünschen.mp3"),
        ("tanzen", "unit13_tanzen.mp3"),
    ],
    "sentences": [
        ("Willkommen zu Kapitel 0.", "chapter00_sentence.mp3"),
        ("Dies ist Kapitel 1.", "chapter01_sentence.mp3"),
        # Add entries for chapters 2-14 here
        ("Wir feiern Weihnachten am 24. Dezember.", "unit13_sent01.mp3"),
        ("Herzlichen Glückwunsch zum Geburtstag!", "unit13_sent02.mp3"),
        ("Ich schenke dir ein Buch.", "unit13_sent03.mp3"),
        ("Ich lade dich zu meiner Party ein.", "unit13_sent04.mp3"),
        ("Frohe Weihnachten und ein gutes neues Jahr!", "unit13_sent05.mp3"),
        ("Wann hast du Geburtstag?", "unit13_sent06.mp3"),
    ],
    "dialogues": [
        ("Hallo! Willkommen zu Kapitel 0.", "chapter00_dialogue.mp3"),
        ("Kapitel 1 beginnt hier.", "chapter01_dialogue.mp3"),
        # Add entries for chapters 2-14 here
        ("Kommst du zu meiner Geburtstagsparty?", "unit13_dialog01.mp3"),
        ("Mama, wann ist Weihnachten?", "unit13_dialog02.mp3"),
        ("Wir heiraten im Juni!", "unit13_dialog03.mp3"),
    ]
}

async def generate_audio(text: str, output_path: str, rate: str = RATE):
    """Generate audio file from text using edge-tts"""
    print(f"Generating audio for: {text} -> {output_path}")
    communicate = edge_tts.Communicate(text, VOICE, rate=rate)
    await communicate.save(output_path)
    print(f"✓ Generated: {output_path}")

async def generate_all():
    """Generate all audio files"""
    base_dir = Path("audio")
    
    # Create directories if they don't exist
    for subdir in ["vocab", "sentences", "dialogues"]:
        (base_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    tasks = []
    
    # Generate vocabulary audio
    for text, filename in audio_data["vocab"]:
        output_path = base_dir / "vocab" / filename
        tasks.append(generate_audio(text, str(output_path)))
    
    # Generate sentence audio
    for text, filename in audio_data["sentences"]:
        output_path = base_dir / "sentences" / filename
        tasks.append(generate_audio(text, str(output_path)))
    
    # Generate dialogue audio
    for text, filename in audio_data["dialogues"]:
        output_path = base_dir / "dialogues" / filename
        tasks.append(generate_audio(text, str(output_path)))
    
    # Run all tasks
    print(f"Generating {len(tasks)} audio files...")
    await asyncio.gather(*tasks)
    print(f"\n✅ All {len(tasks)} audio files generated successfully!")
    print(f"📁 Files saved in: {base_dir.absolute()}")

if __name__ == "__main__":
    asyncio.run(generate_all())
