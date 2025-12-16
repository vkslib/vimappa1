#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Chapter 12 German audio files (Hotel and Travel)
"""
import asyncio
import edge_tts
import os

async def create_chapter_12_audio():
    """Create Chapter 12 audio files"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 12 - Hotel und Reisen (Hotel and Travel)
    sentences = {
        "zimmer_reservieren.mp3": "Ich möchte ein Zimmer reservieren.",
        "einzelzimmer_doppelzimmer.mp3": "Ein Einzelzimmer oder Doppelzimmer?",
        "schluessel_bitte.mp3": "Den Schlüssel, bitte.",
        "fruehstueck_inklusive.mp3": "Ist das Frühstück inklusive?",
        "wlan_password.mp3": "Wie ist das WLAN-Passwort?",
        "rechnung_bezahlen.mp3": "Ich möchte die Rechnung bezahlen.",
        "auschecken_wann.mp3": "Wann muss ich auschecken?",
        "koffer_zimmer.mp3": "Können Sie meinen Koffer aufs Zimmer bringen?",
        "tourist_information.mp3": "Wo ist die Touristeninformation?",
        "stadtplan_haben.mp3": "Haben Sie einen Stadtplan?"
    }
    
    dialogues = {
        "d12_01.mp3": "Guten Abend! Haben Sie ein Zimmer frei?",
        "d12_02.mp3": "Ja, für wie viele Nächte?",
        "d12_03.mp3": "Für drei Nächte.",
        "d12_04.mp3": "Ein Einzelzimmer kostet 89 Euro pro Nacht.",
        "d12_05.mp3": "Das ist in Ordnung.",
        "d12_06.mp3": "Hier ist Ihr Schlüssel, Zimmer 205.",
        "d12_07.mp3": "Wo ist der Aufzug?",
        "d12_08.mp3": "Geradeaus und dann rechts.",
        "d12_09.mp3": "Gibt es hier einen Safe?",
        "d12_10.mp3": "Ja, in Ihrem Zimmer.",
        "d12_11.mp3": "Wann gibt es Frühstück?",
        "d12_12.mp3": "Von 7 bis 10 Uhr im Erdgeschoss.",
        "d12_13.mp3": "Können Sie mir ein Taxi rufen?",
        "d12_14.mp3": "Gern, wohin möchten Sie?",
        "d12_15.mp3": "Zum Bahnhof, bitte."
    }
    
    print("🔊 Creating Chapter 12 German audio files...")
    
    # Create sentences
    print(f"\n📝 Creating {len(sentences)} Chapter 12 sentence audio files...")
    for filename, text in sentences.items():
        filepath = f"audio/sentences/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.2)  # Small delay to prevent issues
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create dialogues
    print(f"\n💬 Creating {len(dialogues)} Chapter 12 dialogue audio files...")
    for filename, text in dialogues.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                await asyncio.sleep(0.2)  # Small delay to prevent issues
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Chapter 12 complete!")

if __name__ == "__main__":
    asyncio.run(create_chapter_12_audio())