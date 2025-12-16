#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German pronunciation exercise audio files
"""
import asyncio
import edge_tts
import os

async def create_exercise_audio():
    """Create audio files for German pronunciation exercises"""
    
    # Create directories if they don't exist
    os.makedirs("audio/pronunciation", exist_ok=True)
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Exercise audio files
    exercise_files = {
        # Missing from previous script
        "v_w_sound.mp3": "Vater, Wasser, vergessen, Wein",
        "vowel_length.mp3": "Stadt, Staat, Mann, Mahn, Bett, Beet",
        
        # Exercise 1: Reading and listening
        "ex1_1.mp3": "Guten Tag! Wie heißen Sie?",
        "ex1_2.mp3": "Ich heiße Anna. Ich komme aus Deutschland.", 
        "ex1_3.mp3": "Sprechen Sie Englisch?",
        
        # Exercise 2: Sound discrimination
        "ex2_1.mp3": "Buch",
        "ex2_2.mp3": "Vater", 
        "ex2_3.mp3": "schön",
        
        # Exercise 3: Spelling example
        "spell_anna.mp3": "A, N, N, A"
    }
    
    print("🔊 Creating German pronunciation exercise audio...")
    
    # Create exercise files
    print(f"\n📝 Creating {len(exercise_files)} exercise audio files...")
    for filename, text in exercise_files.items():
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
    
    print("\n✅ Exercise audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_exercise_audio())