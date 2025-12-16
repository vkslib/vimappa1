import asyncio
import edge_tts

# Missing vocabulary words
missing_vocab = {
    'sie_plural': 'sie',  # They (plural)
    'buch': 'Buch'        # Book
}

async def generate_missing_vocab():
    """Generate missing vocabulary audio files"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    print("Creating missing vocabulary audio files...")
    
    for filename, word in missing_vocab.items():
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            # Create TTS
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            
            # Save to file
            await communicate.save(output_file)
            
            print(f"Created: {word} -> {output_file}")
            
        except Exception as e:
            print(f"Error creating {filename}.mp3: {e}")

if __name__ == "__main__":
    asyncio.run(generate_missing_vocab())
    print("Finished creating missing vocabulary audio!")