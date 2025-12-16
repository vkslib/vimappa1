#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Chapter 13 German audio files (Culture and Going Out)
"""
import asyncio
import edge_tts
import os

async def create_chapter_13_audio():
    """Create Chapter 13 audio files"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 13 - Kultur und Ausgehen (Culture and Going Out)
    sentences = {
        "konzert_besuchen.mp3": "Wir besuchen ein Konzert.",
        "theater_karten.mp3": "Haben Sie noch Karten für das Theater?",
        "museum_oeffnungszeiten.mp3": "Wie sind die Öffnungszeiten vom Museum?",
        "ausstellung_interessant.mp3": "Die Ausstellung ist sehr interessant.",
        "kino_film.mp3": "Welcher Film läuft im Kino?",
        "restaurant_reservierung.mp3": "Ich hätte gern eine Reservierung.",
        "kellner_rechnung.mp3": "Herr Kellner, die Rechnung bitte!",
        "cafe_kuchen.mp3": "Im Café gibt es leckeren Kuchen.",
        "bar_cocktail.mp3": "In der Bar trinken wir einen Cocktail.",
        "disco_tanzen.mp3": "In der Disco können wir tanzen."
    }
    
    dialogues = {
        "d13_01.mp3": "Was machen wir heute Abend?",
        "d13_02.mp3": "Wir könnten ins Kino gehen.",
        "d13_03.mp3": "Gute Idee! Was läuft denn?",
        "d13_04.mp3": "Ein neuer Actionfilm.",
        "d13_05.mp3": "Um wie viel Uhr beginnt er?",
        "d13_06.mp3": "Um 20:15 Uhr.",
        "d13_07.mp3": "Haben Sie einen Tisch für zwei Personen?",
        "d13_08.mp3": "Ja, am Fenster oder lieber in der Mitte?",
        "d13_09.mp3": "Am Fenster, bitte.",
        "d13_10.mp3": "Die Speisekarte, bitte.",
        "d13_11.mp3": "Was können Sie empfehlen?",
        "d13_12.mp3": "Unser Schnitzel ist sehr beliebt.",
        "d13_13.mp3": "Dann nehme ich das Schnitzel.",
        "d13_14.mp3": "Und was möchten Sie trinken?",
        "d13_15.mp3": "Ein Bier, bitte."
    }
    
    print("🔊 Creating Chapter 13 German audio files...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 13 sentence audio files...")
    for filename, text in sentences.items():
        filepath = f"audio/sentences/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.3)  # Delay to prevent connection issues
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create dialogues
    print(f"\n💬 Creating {len(dialogues)} Chapter 13 dialogue audio files...")
    for filename, text in dialogues.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.3)  # Delay to prevent connection issues
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Chapter 13 complete!")

if __name__ == "__main__":
    asyncio.run(create_chapter_13_audio())