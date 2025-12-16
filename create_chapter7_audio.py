#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German sentences and dialogues audio files for chapter 7
"""
import asyncio
import edge_tts
import os

async def create_chapter7_audio():
    """Create missing audio files for chapter 7"""
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Chapter 7 - Sentences
    ch7_sentences = {
        "kann_schwimmen.mp3": "Ich kann sehr gut schwimmen.",
        "spielt_gitarre.mp3": "Er spielt Gitarre in einer Band.",
        "was_hobbys.mp3": "Was sind deine Hobbys?",
        "wochenende_kino.mp3": "Am Wochenende gehe ich ins Kino.",
        "lese_buch.mp3": "Ich lese gern ein gutes Buch.",
        "tennis_spielen.mp3": "Möchtest du Tennis spielen?",
        "oft_joggen.mp3": "Wie oft gehst du joggen?",
        "fussball_spass.mp3": "Fußball macht mir großen Spaß.",
        "hoert_musik.mp3": "Sie hört gern klassische Musik.",
        "museum_interessant.mp3": "Das Museum ist sehr interessant."
    }
    
    # Chapter 7 - Dialogues  
    ch7_dialogues = {
        "d7_01.mp3": "Was machst du in deiner Freizeit?",
        "d7_02.mp3": "Ich spiele gern Fußball und Tennis.",
        "d7_03.mp3": "Welchen Sport treibst du?",
        "d7_04.mp3": "Ich gehe oft schwimmen und joggen.",
        "d7_05.mp3": "Spielst du auch ein Instrument?",
        "d7_06.mp3": "Ja, ich spiele Klavier seit 5 Jahren.",
        "d7_07.mp3": "Gehst du oft ins Kino?",
        "d7_08.mp3": "Ja, besonders gern Actionfilme.",
        "d7_09.mp3": "Was für Musik hörst du?",
        "d7_10.mp3": "Ich höre gern Pop und Rockmusik.",
        "d7_11.mp3": "Liest du auch gern Bücher?",
        "d7_12.mp3": "Ja, vor allem Krimis und Romane.",
        "d7_13.mp3": "Hast du Lust auf ein Konzert?",
        "d7_14.mp3": "Ja, sehr gern! Wann ist es?",
        "d7_15.mp3": "Am Freitagabend um 20 Uhr.",
        "d7_16.mp3": "Perfect! Treffen wir uns um 19:30?"
    }
    
    # Missing d6_18 from Chapter 6
    missing_ch6 = {
        "d6_18.mp3": "Und 4 Euro zurück. Vielen Dank!"
    }
    
    print("🔊 Creating missing German audio files for Chapter 7...")
    
    # Create missing Chapter 6 file first
    print(f"\n🔧 Creating missing Chapter 6 file...")
    for filename, text in missing_ch6.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create Chapter 7 sentence files
    print(f"\n📝 Creating {len(ch7_sentences)} Chapter 7 sentence audio files...")
    for filename, text in ch7_sentences.items():
        filepath = f"audio/sentences/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create Chapter 7 dialogue files
    print(f"\n💬 Creating {len(ch7_dialogues)} Chapter 7 dialogue audio files...")
    for filename, text in ch7_dialogues.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Chapter 7 audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_chapter7_audio())