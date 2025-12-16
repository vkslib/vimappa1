#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German Umlaut and pronunciation audio files
"""
import asyncio
import edge_tts
import os

async def create_umlaut_audio():
    """Create audio files for German Umlauts and pronunciation examples"""
    
    # Create directories if they don't exist
    os.makedirs("audio/alphabet", exist_ok=True)
    os.makedirs("audio/pronunciation", exist_ok=True)
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Umlaut audio files
    umlaut_files = {
        "ae.mp3": "ä",          # a-Umlaut
        "oe.mp3": "ö",          # o-Umlaut  
        "ue.mp3": "ü",          # u-Umlaut
        "ss.mp3": "ß"           # Eszett
    }
    
    # Pronunciation example files
    pronunciation_files = {
        "r_sound.mp3": "Rot, Ruhe, richtig",
        "ch_sound.mp3": "ich, Buch, machen", 
        "umlaut_practice.mp3": "schön, über, Käse, Tür",
        "z_s_sound.mp3": "Zeit, Sonne, Haus"
    }
    
    print("🔊 Creating German Umlaut and pronunciation audio...")
    
    # Create Umlaut files
    print(f"\n📝 Creating {len(umlaut_files)} Umlaut audio files...")
    for filename, text in umlaut_files.items():
        filepath = f"audio/alphabet/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    # Create pronunciation example files  
    print(f"\n📝 Creating {len(pronunciation_files)} pronunciation audio files...")
    for filename, text in pronunciation_files.items():
        filepath = f"audio/pronunciation/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Umlaut and pronunciation audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_umlaut_audio())