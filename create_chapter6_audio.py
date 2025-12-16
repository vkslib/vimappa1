#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German sentences and dialogues audio files for chapters 6 and 7
"""
import asyncio
import edge_tts
import os

async def create_chapters_6_7_audio():
    """Create missing audio files for chapters 6 and 7"""
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Chapter 6 - Sentences
    ch6_sentences = {
        "wie_viel_kostet_buch.mp3": "Wie viel kostet das Buch?",
        "kostet_15_euro.mp3": "Das kostet 15 Euro.",
        "kaufe_zwei_aepfel.mp3": "Ich kaufe zwei Äpfel.",
        "brauche_neue_schuhe.mp3": "Ich brauche neue Schuhe.",
        "zu_teuer.mp3": "Das ist zu teuer!",
        "wo_bezahlen.mp3": "Wo kann ich bezahlen?",
        "nehme_hemd.mp3": "Ich nehme das Hemd.",
        "groesse_m.mp3": "Haben Sie das in Größe M?",
        "supermarkt_geoeffnet.mp3": "Der Supermarkt ist geöffnet.",
        "suche_tasche.mp3": "Ich suche eine Tasche."
    }
    
    # Chapter 6 - Dialogues  
    ch6_dialogues = {
        "d6_01.mp3": "Entschuldigung, wo finde ich Brot?",
        "d6_02.mp3": "Das Brot ist dort hinten links.",
        "d6_03.mp3": "Danke! Wie viel kostet das Brot?",
        "d6_04.mp3": "2 Euro 50.",
        "d6_05.mp3": "Guten Tag! Kann ich Ihnen helfen?",
        "d6_06.mp3": "Ja, ich suche eine Hose.",
        "d6_07.mp3": "Welche Größe brauchen Sie?",
        "d6_08.mp3": "Größe 38, bitte.",
        "d6_09.mp3": "Hier, bitte. Die Hose kostet 49 Euro.",
        "d6_10.mp3": "Kann ich das anprobieren?",
        "d6_11.mp3": "Natürlich! Die Umkleidekabine ist dort.",
        "d6_12.mp3": "Frisches Obst! Äpfel, Bananen, Orangen!",
        "d6_13.mp3": "Was kosten die Äpfel?",
        "d6_14.mp3": "3 Euro pro Kilo.",
        "d6_15.mp3": "Ich nehme zwei Kilo, bitte.",
        "d6_16.mp3": "Das macht 6 Euro. Sonst noch etwas?",
        "d6_17.mp3": "Nein, danke. Hier sind 10 Euro.",
        "d6_18.mp3": "Und 4 Euro zurück. Vielen Dank!"
    }
    
    print("🔊 Creating missing German audio files for Chapter 6...")
    
    # Create Chapter 6 sentence files
    print(f"\n📝 Creating {len(ch6_sentences)} Chapter 6 sentence audio files...")
    for filename, text in ch6_sentences.items():
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
    
    # Create Chapter 6 dialogue files
    print(f"\n💬 Creating {len(ch6_dialogues)} Chapter 6 dialogue audio files...")
    for filename, text in ch6_dialogues.items():
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
    
    print("\n✅ Chapter 6 audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_chapters_6_7_audio())