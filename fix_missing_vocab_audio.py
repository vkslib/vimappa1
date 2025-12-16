import asyncio
import edge_tts
import re
import os
from pathlib import Path

# Missing vocabulary that needs to be created based on chapter analysis
missing_vocab_unit7 = {
    'fussball': 'Fußball',
    'tennis': 'Tennis',
    'schwimmen': 'schwimmen',
    'joggen': 'joggen',
    'radfahren': 'Rad fahren',
    'basketball': 'Basketball'
}

missing_vocab_general = {
    'lesen': 'lesen',
    'malen': 'malen',
    'kochen': 'kochen', 
    'tanzen': 'tanzen',
    'singen': 'singen',
    'musik_hoeren': 'Musik hören',
    'fotografieren': 'fotografieren',
    'wandern': 'wandern'
}

async def create_missing_vocab():
    """Create missing vocabulary audio files"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    all_missing = {**missing_vocab_unit7, **missing_vocab_general}
    
    print(f"Creating {len(all_missing)} missing vocabulary audio files...")
    
    for filename, word in all_missing.items():
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            # Skip if file already exists
            if os.path.exists(output_file):
                print(f"Skipped: {filename}.mp3 (already exists)")
                continue
                
            # Create TTS
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            
            # Save to file
            await communicate.save(output_file)
            
            print(f"Created: {word} -> {output_file}")
            
        except Exception as e:
            print(f"Error creating {filename}.mp3: {e}")

def find_missing_audio_paths():
    """Find all missing audio paths in chapter files"""
    chapter_dir = Path("chapters")
    missing_files = []
    
    for chapter_file in chapter_dir.glob("*.html"):
        print(f"\nChecking {chapter_file.name}...")
        
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all audio paths
        audio_matches = re.findall(r"play\('\.\.\/audio\/vocab\/([^']+\.mp3)'\)", content)
        
        for audio_file in audio_matches:
            audio_path = f"audio/vocab/{audio_file}"
            if not os.path.exists(audio_path):
                missing_files.append({
                    'chapter': chapter_file.name,
                    'audio_file': audio_file,
                    'path': audio_path
                })
                print(f"  ❌ Missing: {audio_file}")
            else:
                print(f"  ✅ Found: {audio_file}")
    
    return missing_files

if __name__ == "__main__":
    print("🔍 Analyzing missing vocabulary audio files...")
    
    # Check for missing files
    missing = find_missing_audio_paths()
    
    if missing:
        print(f"\n⚠️  Found {len(missing)} missing audio files:")
        for item in missing:
            print(f"  📂 {item['chapter']}: {item['audio_file']}")
    
    # Create missing vocab files
    print(f"\n🔊 Creating missing vocabulary audio...")
    asyncio.run(create_missing_vocab())
    
    print(f"\n✅ Vocabulary audio creation complete!")
    print(f"🎯 Check your website - all vocab should have audio now!")