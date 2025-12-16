import asyncio
import edge_tts
import os

# Final batch - Health and Body vocabulary
health_vocab = {
    'spazieren_gehen': 'spazieren gehen',
    'treffen': 'treffen',
    'spiel': 'Spiel',
    'computerspiel': 'Computerspiel',
    'freizeit': 'Freizeit',
    'hobby': 'Hobby',
    'spass': 'Spaß',
    'interessant': 'interessant',
    'kopf': 'Kopf',
    'bauch': 'Bauch',
    'ruecken': 'Rücken',
    'bein': 'Bein',
    'arm': 'Arm',
    'hand': 'Hand',
    'fuss': 'Fuß',
    'auge': 'Auge',
    'ohr': 'Ohr',
    'nase': 'Nase',
    'mund': 'Mund',
    'zahn': 'Zahn',
    'fieber': 'Fieber',
    'husten': 'Husten',
    'schnupfen': 'Schnupfen',
    'grippe': 'Grippe',
    'erkaeltung': 'Erkältung',
    'kopfschmerzen': 'Kopfschmerzen',
    'bauchschmerzen': 'Bauchschmerzen',
    'halsschmerzen': 'Halsschmerzen',
    'krankenhaus': 'Krankenhaus',
    'medikament': 'Medikament',
    'tablette': 'Tablette',
    'wehtun': 'wehtun',
    'krank_sein': 'krank sein',
    'gesund_sein': 'gesund sein',
    'ausruhen': 'ausruhen',
    'untersuchen': 'untersuchen',
    'helfen': 'helfen'
}

async def create_health_vocab():
    """Create health vocabulary batch"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    print(f"🔊 Creating final batch: {len(health_vocab)} health vocabulary files...")
    
    for i, (filename, word) in enumerate(health_vocab.items(), 1):
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            if os.path.exists(output_file):
                print(f"[{i:2}/{len(health_vocab)}] ⏭️  Skipped: {filename}.mp3")
                continue
                
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            await communicate.save(output_file)
            
            print(f"[{i:2}/{len(health_vocab)}] ✅ Created: {word} -> {filename}.mp3")
            
            if i % 5 == 0:
                await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"[{i:2}/{len(health_vocab)}] ❌ Error: {filename}.mp3 - {e}")

if __name__ == "__main__":
    print("🚀 Creating final health vocabulary batch...")
    asyncio.run(create_health_vocab())
    print("✅ Final batch complete!")