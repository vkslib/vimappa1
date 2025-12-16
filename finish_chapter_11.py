#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finish Chapter 11 missing German dialogue audio files
"""
import asyncio
import edge_tts
import os
import time

async def create_chapter_11_remaining():
    """Create remaining Chapter 11 dialogue files"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Remaining Chapter 11 dialogues that need to be created
    remaining_dialogues = {
        "d11_11.mp3": "Nein, aber es ist sehr bewölkt.",
        "d11_12.mp3": "Dann werden wir wohl nass.",
        "d11_13.mp3": "Hoffentlich nicht!",
        "d11_14.mp3": "Magst du den Winter?",
        "d11_15.mp3": "Ja, ich liebe Schnee!"
    }
    
    print("🔊 Creating remaining Chapter 11 dialogue audio files...")
    
    for filename, text in remaining_dialogues.items():
        filepath = f"audio/dialogues/{filename}"
        if not os.path.exists(filepath):
            try:
                communicate = edge_tts.Communicate(text, voice, rate=rate)
                await communicate.save(filepath)
                print(f"✅ Created: {filename} -> {text}")
                
                # Add small delay to prevent timeout
                await asyncio.sleep(0.5)
                
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
                # Add delay on error and retry once
                await asyncio.sleep(2)
                try:
                    communicate = edge_tts.Communicate(text, voice, rate=rate)
                    await communicate.save(filepath)
                    print(f"✅ Retry success: {filename}")
                except Exception as retry_error:
                    print(f"❌ Retry failed for {filename}: {retry_error}")
        else:
            print(f"⏭️  Skipped: {filename} (already exists)")
    
    print("\n✅ Chapter 11 completion finished!")

if __name__ == "__main__":
    asyncio.run(create_chapter_11_remaining())