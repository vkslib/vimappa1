import asyncio
import edge_tts
import os

# Missing alphabet letters
missing_letters = {
    'w': 'Ve',
    'x': 'Iks', 
    'y': 'Ypsilon',
    'z': 'Zet'
}

async def generate_missing_audio():
    """Generate missing alphabet audio files"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/alphabet"
    
    print("Creating missing German alphabet audio files...")
    
    for letter, pronunciation in missing_letters.items():
        try:
            output_file = f"{output_dir}/{letter}.mp3"
            
            # Create TTS
            communicate = edge_tts.Communicate(pronunciation, voice, rate="-20%")
            
            # Save to file
            await communicate.save(output_file)
            
            print(f"Created: {letter.upper()} -> {pronunciation} -> {output_file}")
            
        except Exception as e:
            print(f"Error creating {letter}.mp3: {e}")

# Run function
if __name__ == "__main__":
    asyncio.run(generate_missing_audio())
    print("Finished creating missing alphabet audio!")