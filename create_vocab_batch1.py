import asyncio
import edge_tts
import os

# Remaining vocabulary that still needs to be created
remaining_vocab = {
    'wasser': 'Wasser',
    'kaffee': 'Kaffee', 
    'tee': 'Tee',
    'saft': 'Saft',
    'bier': 'Bier',
    'wein': 'Wein',
    'fruehstueck': 'Frühstück',
    'mittagessen': 'Mittagessen', 
    'abendessen': 'Abendessen',
    'restaurant': 'Restaurant',
    'speisekarte': 'Speisekarte',
    'rechnung': 'Rechnung',
    'supermarkt': 'Supermarkt',
    'geschaeft': 'Geschäft',
    'markt': 'Markt',
    'baeckerei': 'Bäckerei',
    'apotheke': 'Apotheke',
    'buchhandlung': 'Buchhandlung',
    'preis': 'Preis',
    'geld': 'Geld',
    'euro': 'Euro',
    'cent': 'Cent',
    'bezahlen': 'bezahlen',
    'kosten': 'kosten',
    'kaufen': 'kaufen',
    'verkaufen': 'verkaufen'
}

async def create_remaining_vocab_batch1():
    """Create remaining vocabulary - batch 1"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    print(f"🔊 Creating batch 1: {len(remaining_vocab)} vocabulary files...")
    
    for i, (filename, word) in enumerate(remaining_vocab.items(), 1):
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            if os.path.exists(output_file):
                print(f"[{i:2}/{len(remaining_vocab)}] ⏭️  Skipped: {filename}.mp3")
                continue
                
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            await communicate.save(output_file)
            
            print(f"[{i:2}/{len(remaining_vocab)}] ✅ Created: {word} -> {filename}.mp3")
            
            # Small delay every 5 files
            if i % 5 == 0:
                await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"[{i:2}/{len(remaining_vocab)}] ❌ Error: {filename}.mp3 - {e}")

if __name__ == "__main__":
    print("🚀 Creating remaining vocabulary batch 1...")
    asyncio.run(create_remaining_vocab_batch1())
    print("✅ Batch 1 complete!")