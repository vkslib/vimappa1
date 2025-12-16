import asyncio
import edge_tts
import os

# Batch 2 - Shopping, Hobbies, Health vocabulary
vocab_batch2 = {
    'brauchen': 'brauchen',
    'suchen': 'suchen', 
    'nehmen': 'nehmen',
    'geben': 'geben',
    'kleidung': 'Kleidung',
    'hemd': 'Hemd',
    'hose': 'Hose',
    'schuhe': 'Schuhe',
    'tasche': 'Tasche',
    'teuer': 'teuer',
    'billig': 'billig',
    'gross': 'groß',
    'klein': 'klein',
    'neu': 'neu',
    'alt': 'alt',
    'gitarre': 'Gitarre',
    'klavier': 'Klavier',
    'musik': 'Musik',
    'hoeren': 'hören',
    'spielen': 'spielen',
    'konzert': 'Konzert',
    'fernsehen': 'fernsehen',
    'kino': 'Kino',
    'theater': 'Theater',
    'museum': 'Museum'
}

async def create_vocab_batch2():
    """Create vocabulary batch 2"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    print(f"🔊 Creating batch 2: {len(vocab_batch2)} vocabulary files...")
    
    for i, (filename, word) in enumerate(vocab_batch2.items(), 1):
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            if os.path.exists(output_file):
                print(f"[{i:2}/{len(vocab_batch2)}] ⏭️  Skipped: {filename}.mp3")
                continue
                
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            await communicate.save(output_file)
            
            print(f"[{i:2}/{len(vocab_batch2)}] ✅ Created: {word} -> {filename}.mp3")
            
            if i % 5 == 0:
                await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"[{i:2}/{len(vocab_batch2)}] ❌ Error: {filename}.mp3 - {e}")

if __name__ == "__main__":
    print("🚀 Creating vocabulary batch 2...")
    asyncio.run(create_vocab_batch2())
    print("✅ Batch 2 complete!")