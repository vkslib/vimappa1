import asyncio
import edge_tts
import os

# All missing vocabulary from chapters 5-8
missing_vocab = {
    # Chapter 5 - Food & Drinks
    'brot': 'Brot',
    'pizza': 'Pizza', 
    'kaese': 'Käse',
    'butter': 'Butter',
    'ei': 'Ei',
    'milch': 'Milch',
    'fleisch': 'Fleisch',
    'fisch': 'Fisch',
    'huhn': 'Huhn',
    'reis': 'Reis',
    'nudeln': 'Nudeln',
    'kartoffel': 'Kartoffel',
    'salat': 'Salat',
    'suppe': 'Suppe',
    'obst': 'Obst',
    'gemuese': 'Gemüse',
    'apfel': 'Apfel',
    'banane': 'Banane',
    'orange': 'Orange',
    'tomate': 'Tomate',
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
    
    # Chapter 6 - Shopping & Numbers
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
    'verkaufen': 'verkaufen',
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
    
    # Chapter 7 - Hobbies (additional to what we created)
    'gitarre': 'Gitarre',
    'klavier': 'Klavier',
    'musik': 'Musik',
    'hoeren': 'hören',
    'spielen': 'spielen',
    'konzert': 'Konzert',
    'fernsehen': 'fernsehen',
    'kino': 'Kino',
    'theater': 'Theater',
    'museum': 'Museum',
    'spazieren_gehen': 'spazieren gehen',
    'treffen': 'treffen',
    'spiel': 'Spiel',
    'computerspiel': 'Computerspiel',
    'freizeit': 'Freizeit',
    'hobby': 'Hobby',
    'spass': 'Spaß',
    'interessant': 'interessant',
    
    # Chapter 8 - Health & Body
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
    'apotheke': 'Apotheke',
    'medikament': 'Medikament',
    'tablette': 'Tablette',
    'wehtun': 'wehtun',
    'krank_sein': 'krank sein',
    'gesund_sein': 'gesund sein',
    'ausruhen': 'ausruhen',
    'untersuchen': 'untersuchen',
    'helfen': 'helfen'
}

async def create_all_missing_vocab():
    """Create ALL missing vocabulary audio files in batches"""
    voice = "de-DE-KatjaNeural"
    output_dir = "audio/vocab"
    
    print(f"🔊 Creating {len(missing_vocab)} missing vocabulary audio files...")
    print("This may take several minutes...")
    
    created_count = 0
    skipped_count = 0
    error_count = 0
    
    for i, (filename, word) in enumerate(missing_vocab.items(), 1):
        try:
            output_file = f"{output_dir}/{filename}.mp3"
            
            # Skip if file already exists
            if os.path.exists(output_file):
                print(f"[{i:3}/{len(missing_vocab)}] ⏭️  Skipped: {filename}.mp3 (exists)")
                skipped_count += 1
                continue
                
            # Create TTS
            communicate = edge_tts.Communicate(word, voice, rate="-20%")
            
            # Save to file
            await communicate.save(output_file)
            
            print(f"[{i:3}/{len(missing_vocab)}] ✅ Created: {word} -> {filename}.mp3")
            created_count += 1
            
            # Small delay to prevent overloading
            if i % 10 == 0:
                await asyncio.sleep(1)
            
        except Exception as e:
            print(f"[{i:3}/{len(missing_vocab)}] ❌ Error: {filename}.mp3 - {e}")
            error_count += 1
    
    print(f"\n🎉 COMPLETED!")
    print(f"✅ Created: {created_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    print(f"❌ Errors: {error_count} files")
    print(f"\n🎯 Total vocabulary audio files: {created_count + skipped_count}")

if __name__ == "__main__":
    print("🚀 Starting comprehensive vocabulary audio creation...")
    asyncio.run(create_all_missing_vocab())
    print("🎓 All vocabulary should now have German audio pronunciation!")
    print("🌐 GitDoc will sync these changes to your website automatically!")