#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German sentences and dialogues audio files for chapters 5, 6, 7
"""
import asyncio
import edge_tts
import os

async def create_missing_audio():
    """Create missing audio files for sentences and dialogues"""
    
    # Create directories if they don't exist
    os.makedirs("audio/sentences", exist_ok=True)
    os.makedirs("audio/dialogues", exist_ok=True)
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Chapter 5 - Sentences
    ch5_sentences = {
        "ich_esse_brot_fruehstueck.mp3": "Ich esse Brot zum Frühstück.",
        "magst_du_pizza.mp3": "Magst du Pizza?",
        "sie_trinkt_kaffee.mp3": "Sie trinkt gern Kaffee.",
        "wir_moegen_obst_gemuese.mp3": "Wir mögen Obst und Gemüse.",
        "isst_du_fleisch_fisch.mp3": "Isst du Fleisch oder Fisch?",
        "mittagessen_reis_huhn.mp3": "Zum Mittagessen esse ich Reis mit Huhn.",
        "trinke_wasser_kein_saft.mp3": "Ich trinke Wasser, keinen Saft.",
        "moechten_speisekarte.mp3": "Möchten Sie die Speisekarte?",
        "rechnung_bitte.mp3": "Die Rechnung, bitte!",
        "esse_gern_schokolade.mp3": "Ich esse gern Schokolade."
    }
    
    # Chapter 5 - Dialogues  
    ch5_dialogues = {
        "d5_01.mp3": "Guten Tag! Was möchten Sie essen?",
        "d5_02.mp3": "Ich möchte Pizza, bitte.",
        "d5_03.mp3": "Und was möchten Sie trinken?",
        "d5_04.mp3": "Ein Wasser, bitte.",
        "d5_05.mp3": "Sehr gern. Kommt sofort!",
        "d5_06.mp3": "Was isst du zum Frühstück?",
        "d5_07.mp3": "Ich esse Brot mit Käse und Butter.",
        "d5_08.mp3": "Trinkst du Kaffee oder Tee?",
        "d5_09.mp3": "Ich trinke Kaffee mit Milch.",
        "d5_10.mp3": "Und isst du auch Obst?",
        "d5_11.mp3": "Ja, ich esse gern Äpfel und Bananen.",
        "d5_12.mp3": "Wir brauchen Milch und Eier.",
        "d5_13.mp3": "Und Brot. Möchtest du auch Fisch kaufen?",
        "d5_14.mp3": "Nein, ich mag keinen Fisch. Lieber Huhn.",
        "d5_15.mp3": "Okay. Kaufen wir auch Obst und Gemüse?",
        "d5_16.mp3": "Ja, wir brauchen Tomaten und Salat."
    }
    
    print("🔊 Creating missing German audio files for Chapter 5...")
    
    # Create Chapter 5 sentence files
    print(f"\n📝 Creating {len(ch5_sentences)} Chapter 5 sentence audio files...")
    for filename, text in ch5_sentences.items():
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
    
    # Create Chapter 5 dialogue files
    print(f"\n💬 Creating {len(ch5_dialogues)} Chapter 5 dialogue audio files...")
    for filename, text in ch5_dialogues.items():
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
    
    print("\n✅ Chapter 5 audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_missing_audio())