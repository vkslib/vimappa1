#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create correct German audio files for Chapter 10 (Travel and Transport)
"""
import asyncio
import edge_tts
import os

async def create_correct_chapter_10_audio():
    """Create correct Chapter 10 audio files for Travel and Transport"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 10 - Reisen und Verkehr (Travel and Transport) - CORRECT sentences
    sentences = {
        "unit10_sent01.mp3": "Ich fahre mit dem Bus zur Arbeit.",
        "unit10_sent02.mp3": "Wir wollen nach Berlin fahren.",
        "unit10_sent03.mp3": "Der Zug fährt um 10 Uhr ab.",
        "unit10_sent04.mp3": "Wann kommst du am Bahnhof an?",
        "unit10_sent05.mp3": "Ich muss in München umsteigen.",
        "unit10_sent06.mp3": "Wo ist die nächste Haltestelle?",
        "unit10_sent07.mp3": "Gehen Sie geradeaus und dann links.",
        "unit10_sent08.mp3": "Ich brauche eine Fahrkarte nach Hamburg.",
        "unit10_sent09.mp3": "Das Flugzeug ist pünktlich angekommen.",
        "unit10_sent10.mp3": "Entschuldigung, wo ist der Ausgang?",
        "unit10_sent11.mp3": "Der Bus hat Verspätung.",
        "unit10_sent12.mp3": "Können Sie mir beim Gepäck helfen?"
    }
    
    # Create dialogues for travel situations
    dialogues = {
        "unit10_dialog01.mp3": "Entschuldigung, wie komme ich zum Bahnhof?",
        "unit10_dialog02.mp3": "Fahren Sie mit der U-Bahn Linie 3.",
        "unit10_dialog03.mp3": "Wie lange dauert das?",
        "unit10_dialog04.mp3": "Ungefähr 15 Minuten.",
        "unit10_dialog05.mp3": "Eine Fahrkarte nach München, bitte.",
        "unit10_dialog06.mp3": "Einfach oder hin und zurück?",
        "unit10_dialog07.mp3": "Hin und zurück, bitte.",
        "unit10_dialog08.mp3": "Das macht 45 Euro.",
        "unit10_dialog09.mp3": "Von welchem Gleis fährt der Zug?",
        "unit10_dialog10.mp3": "Von Gleis 7.",
        "unit10_dialog11.mp3": "Wann ist der nächste Zug nach Frankfurt?",
        "unit10_dialog12.mp3": "In 20 Minuten.",
        "unit10_dialog13.mp3": "Ist das ein direkter Zug?",
        "unit10_dialog14.mp3": "Nein, Sie müssen in Mannheim umsteigen.",
        "unit10_dialog15.mp3": "Gute Reise!"
    }
    
    print("🔊 Creating correct Chapter 10 German audio files (Travel and Transport)...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 10 sentence audio files...")
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
    print(f"\n💬 Creating {len(dialogues)} Chapter 10 dialogue audio files...")
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
    
    print("\n✅ Chapter 10 Travel and Transport audio complete!")

if __name__ == "__main__":
    asyncio.run(create_correct_chapter_10_audio())