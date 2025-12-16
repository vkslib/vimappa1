#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Chapter 14 German audio files (Exam Preparation)
"""
import asyncio
import edge_tts
import os

async def create_chapter_14_audio():
    """Create Chapter 14 audio files"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 14 - Prüfungsvorbereitung (Exam Preparation)
    sentences = {
        "deutsch_lernen.mp3": "Ich lerne seit einem Jahr Deutsch.",
        "pruefung_schwer.mp3": "Die Prüfung war sehr schwer.",
        "grammatik_ueben.mp3": "Ich muss mehr Grammatik üben.",
        "vokabeln_wiederholen.mp3": "Wir wiederholen die Vokabeln.",
        "sprechen_verbessern.mp3": "Mein Sprechen muss sich verbessern.",
        "hoeren_verstehen.mp3": "Das Hören und Verstehen ist wichtig.",
        "schreiben_ueben.mp3": "Ich übe das Schreiben jeden Tag.",
        "lesen_macht_spass.mp3": "Lesen macht mir großen Spaß.",
        "kurs_beendet.mp3": "Der Kurs ist fast beendet.",
        "zertifikat_bekommen.mp3": "Ich bekomme hoffentlich das Zertifikat."
    }
    
    dialogues = {
        "d14_01.mp3": "Bist du nervös wegen der Prüfung?",
        "d14_02.mp3": "Ja, sehr! Und du?",
        "d14_03.mp3": "Auch ein bisschen.",
        "d14_04.mp3": "Hast du gut gelernt?",
        "d14_05.mp3": "Ich hoffe es! Jeden Tag zwei Stunden.",
        "d14_06.mp3": "Was war am schwierigsten für dich?",
        "d14_07.mp3": "Die Grammatik, besonders die Artikel.",
        "d14_08.mp3": "Das verstehe ich gut.",
        "d14_09.mp3": "Wie lange lernst du schon Deutsch?",
        "d14_10.mp3": "Seit acht Monaten.",
        "d14_11.mp3": "Warum lernst du Deutsch?",
        "d14_12.mp3": "Ich möchte in Deutschland studieren.",
        "d14_13.mp3": "Das ist ein guter Grund!",
        "d14_14.mp3": "Viel Erfolg bei der Prüfung!",
        "d14_15.mp3": "Danke! Dir auch!"
    }
    
    print("🔊 Creating Chapter 14 German audio files...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 14 sentence audio files...")
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
    print(f"\n💬 Creating {len(dialogues)} Chapter 14 dialogue audio files...")
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
    
    print("\n✅ Chapter 14 complete!")

if __name__ == "__main__":
    asyncio.run(create_chapter_14_audio())