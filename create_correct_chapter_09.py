#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create correct German audio files for Chapter 9 (Weather and Seasons)
"""
import asyncio
import edge_tts
import os

async def create_correct_chapter_09_audio():
    """Create correct Chapter 9 audio files for Weather and Seasons"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 9 - Wetter und Jahreszeiten (Weather and Seasons) - CORRECT sentences
    sentences = {
        "unit09_sent01.mp3": "Wie ist das Wetter heute?",
        "unit09_sent02.mp3": "Heute ist es sonnig und warm.",
        "unit09_sent03.mp3": "Es regnet den ganzen Tag.",
        "unit09_sent04.mp3": "Im Winter schneit es oft in Deutschland.",
        "unit09_sent05.mp3": "Im Frühling ist das Wetter sehr schön.",
        "unit09_sent06.mp3": "Der Sommer ist heiß und trocken.",
        "unit09_sent07.mp3": "Im Herbst ist es oft windig und kühl.",
        "unit09_sent08.mp3": "Die Temperatur ist 20 Grad.",
        "unit09_sent09.mp3": "Ich brauche einen Regenschirm.",
        "unit09_sent10.mp3": "Im Januar ist es sehr kalt.",
        "unit09_sent11.mp3": "Heute gibt es ein Gewitter.",
        "unit09_sent12.mp3": "Morgen wird es bewölkt sein."
    }
    
    # Create dialogues mapping based on what we see in HTML
    dialogues = {
        "unit09_dialog01.mp3": "Wie ist das Wetter heute?",
        "unit09_dialog02.mp3": "Es ist sehr schön und sonnig.",
        "unit09_dialog03.mp3": "Perfekt für einen Spaziergang!",
        "unit09_dialog04.mp3": "Wird es morgen auch so schön?",
        "unit09_dialog05.mp3": "Nein, morgen soll es regnen.",
        "unit09_dialog06.mp3": "Dann brauche ich einen Regenschirm.",
        "unit09_dialog07.mp3": "Im Winter ist es immer so kalt hier.",
        "unit09_dialog08.mp3": "Ja, aber der Schnee ist wunderschön.",
        "unit09_dialog09.mp3": "Welche Jahreszeit magst du am liebsten?",
        "unit09_dialog10.mp3": "Ich liebe den Frühling!",
        "unit09_dialog11.mp3": "Die Blumen blühen und es wird wärmer.",
        "unit09_dialog12.mp3": "Im Sommer fahren wir oft an den Strand.",
        "unit09_dialog13.mp3": "Das klingt sehr schön.",
        "unit09_dialog14.mp3": "Der Herbst ist auch sehr romantisch.",
        "unit09_dialog15.mp3": "Ja, die bunten Blätter sind wunderschön."
    }
    
    print("🔊 Creating correct Chapter 9 German audio files (Weather and Seasons)...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 9 sentence audio files...")
    for filename, text in sentences.items():
        filepath = f"audio/sentences/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.3)
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create dialogues
    print(f"\n💬 Creating {len(dialogues)} Chapter 9 dialogue audio files...")
    for filename, text in dialogues.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.3)
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Chapter 9 Weather and Seasons audio complete!")

if __name__ == "__main__":
    asyncio.run(create_correct_chapter_09_audio())