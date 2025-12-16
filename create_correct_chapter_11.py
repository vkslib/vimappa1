#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create correct German audio files for Chapter 11 (School and Learning)
"""
import asyncio
import edge_tts
import os

async def create_correct_chapter_11_audio():
    """Create correct Chapter 11 audio files for School and Learning"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 11 - Schule und Lernen (School and Learning) - CORRECT sentences
    sentences = {
        "unit11_sent01.mp3": "Ich lerne Deutsch.",
        "unit11_sent02.mp3": "Wir haben Mathematik und Englisch.",
        "unit11_sent03.mp3": "Die Schüler machen Hausaufgaben.",
        "unit11_sent04.mp3": "Der Lehrer schreibt an die Tafel.",
        "unit11_sent05.mp3": "Ich habe Deutsch gelernt.",
        "unit11_sent06.mp3": "Darf ich eine Frage stellen?",
        "unit11_sent07.mp3": "Die Prüfung ist sehr schwer.",
        "unit11_sent08.mp3": "Ich verstehe die Grammatik nicht.",
        "unit11_sent09.mp3": "Können Sie das bitte wiederholen?",
        "unit11_sent10.mp3": "Der Unterricht beginnt um 8 Uhr."
    }
    
    # Create dialogues for school situations
    dialogues = {
        "unit11_dialog01.mp3": "Guten Morgen! Wie geht es dir?",
        "unit11_dialog02.mp3": "Gut, danke! Hast du die Hausaufgaben gemacht?",
        "unit11_dialog03.mp3": "Ja, aber es war sehr schwer.",
        "unit11_dialog04.mp3": "Können wir zusammen lernen?",
        "unit11_dialog05.mp3": "Gute Idee! Nach dem Unterricht?",
        "unit11_dialog06.mp3": "Entschuldigung, ich verstehe nicht.",
        "unit11_dialog07.mp3": "Können Sie das bitte erklären?",
        "unit11_dialog08.mp3": "Natürlich, gerne.",
        "unit11_dialog09.mp3": "Welche Fächer haben wir heute?",
        "unit11_dialog10.mp3": "Deutsch, Mathematik und Geschichte.",
        "unit11_dialog11.mp3": "Wann ist die nächste Prüfung?",
        "unit11_dialog12.mp3": "Nächste Woche Mittwoch.",
        "unit11_dialog13.mp3": "Dann muss ich viel lernen.",
        "unit11_dialog14.mp3": "Ja, wir können zusammen üben.",
        "unit11_dialog15.mp3": "Das ist eine gute Idee!"
    }
    
    print("🔊 Creating correct Chapter 11 German audio files (School and Learning)...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 11 sentence audio files...")
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
    print(f"\n💬 Creating {len(dialogues)} Chapter 11 dialogue audio files...")
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
    
    print("\n✅ Chapter 11 School and Learning audio complete!")

if __name__ == "__main__":
    asyncio.run(create_correct_chapter_11_audio())