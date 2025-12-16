import asyncio
import edge_tts
import os

# German alphabet with pronunciation
alphabet_words = {
    'a': 'A',
    'b': 'Be', 
    'c': 'Ce',
    'd': 'De',
    'e': 'E',
    'f': 'Ef',
    'g': 'Ge',
    'h': 'Ha',
    'i': 'I',
    'j': 'Jot',
    'k': 'Ka',
    'l': 'El',
    'm': 'Em',
    'n': 'En',
    'o': 'O',
    'p': 'Pe',
    'q': 'Ku',
    'r': 'Er',
    's': 'Es',
    't': 'Te',
    'u': 'U',
    'v': 'Fau',
    'w': 'Ve',
    'x': 'Iks',
    'y': 'Ypsilon',
    'z': 'Zet'
}

async def generate_alphabet_audio():
    """Generate audio files for German alphabet"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/alphabet"
    
    print("Creating German alphabet audio files...")
    print(f"Output directory: {output_dir}")
    
    for letter, pronunciation in alphabet_words.items():
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
    print("Starting German alphabet audio generation...")
    asyncio.run(generate_alphabet_audio())
    print("Finished! All alphabet letters have audio files.")