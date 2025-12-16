#!/usr/bin/env python3
"""
Generate German audio files for Units 5-14 using edge-tts
"""
import asyncio
import edge_tts
import os
from pathlib import Path

# German voice (female, clear for learning)
VOICE = "de-DE-KatjaNeural"
# Slow rate for A1 learners (-20% speed)
RATE = "-20%"

# Base directory
BASE_DIR = Path(__file__).parent / "audio"

async def generate_audio(text, filename, subfolder="vocab", max_retries=3):
    """Generate single audio file with retry logic"""
    output_dir = BASE_DIR / subfolder
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    
    if output_path.exists():
        print(f"Skipping {filename} (already exists)")
        return True
    
    for attempt in range(max_retries):
        try:
            communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
            await communicate.save(str(output_path))
            print(f"✓ Generated: {filename}")
            await asyncio.sleep(0.5)  # Small delay between files
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"⚠ Error on attempt {attempt + 1} for {filename}, retrying...")
                await asyncio.sleep(3)  # Wait 3 seconds before retry
            else:
                print(f"✗ Failed to generate {filename} after {max_retries} attempts: {e}")
                return False

async def generate_all():
    """Generate all audio files for Units 5-14"""
    
    # Unit 5: Essen und Trinken
    unit05_vocab = [
        ("das Brot", "unit05_brot.mp3"),
        ("der Käse", "unit05_kaese.mp3"),
        ("die Pizza", "unit05_pizza.mp3"),
        ("die Wurst", "unit05_wurst.mp3"),
        ("das Fleisch", "unit05_fleisch.mp3"),
        ("der Fisch", "unit05_fisch.mp3"),
        ("das Ei", "unit05_ei.mp3"),
        ("der Salat", "unit05_salat.mp3"),
        ("die Suppe", "unit05_suppe.mp3"),
        ("das Obst", "unit05_obst.mp3"),
        ("das Gemüse", "unit05_gemuese.mp3"),
        ("der Apfel", "unit05_apfel.mp3"),
        ("die Banane", "unit05_banane.mp3"),
        ("die Tomate", "unit05_tomate.mp3"),
        ("die Kartoffel", "unit05_kartoffel.mp3"),
        ("der Reis", "unit05_reis.mp3"),
        ("die Nudeln", "unit05_nudeln.mp3"),
        ("der Zucker", "unit05_zucker.mp3"),
        ("das Salz", "unit05_salz.mp3"),
        ("das Wasser", "unit05_wasser.mp3"),
        ("der Kaffee", "unit05_kaffee.mp3"),
        ("der Tee", "unit05_tee.mp3"),
        ("die Milch", "unit05_milch.mp3"),
        ("der Saft", "unit05_saft.mp3"),
        ("das Bier", "unit05_bier.mp3"),
        ("der Wein", "unit05_wein.mp3"),
        ("mögen", "unit05_moegen.mp3"),
        ("essen", "unit05_essen.mp3"),
        ("trinken", "unit05_trinken.mp3"),
        ("schmecken", "unit05_schmecken.mp3"),
    ]
    
    unit05_sentences = [
        ("Ich esse Brot und Käse.", "unit05_sent01.mp3"),
        ("Magst du Pizza?", "unit05_sent02.mp3"),
        ("Ich trinke gern Kaffee.", "unit05_sent03.mp3"),
        ("Das Essen schmeckt gut.", "unit05_sent04.mp3"),
        ("Ich möchte Wasser, bitte.", "unit05_sent05.mp3"),
        ("Was isst du zum Frühstück?", "unit05_sent06.mp3"),
        ("Ich mag Obst und Gemüse.", "unit05_sent07.mp3"),
        ("Trinkst du Tee oder Kaffee?", "unit05_sent08.mp3"),
        ("Das schmeckt sehr lecker!", "unit05_sent09.mp3"),
        ("Ich esse gern Fisch.", "unit05_sent10.mp3"),
    ]
    
    unit05_dialogues = [
        ("Im Restaurant. Anna: Guten Tag! Was möchten Sie essen? Tom: Ich möchte eine Pizza, bitte. Anna: Und zum Trinken? Tom: Ein Wasser, bitte. Anna: Sehr gern. Das kostet 12 Euro.", "unit05_dialog01.mp3"),
        ("Beim Frühstück. Mutter: Was isst du zum Frühstück? Kind: Ich esse Brot mit Butter und Marmelade. Mutter: Möchtest du auch Obst? Kind: Ja, ich mag Äpfel und Bananen. Mutter: Hier, nimm einen Apfel. Und trink deine Milch! Kind: Danke, Mama!", "unit05_dialog02.mp3"),
        ("Im Supermarkt. Tom: Entschuldigung, wo finde ich Obst und Gemüse? Verkäufer: Da hinten, auf der linken Seite. Tom: Danke! Und haben Sie frischen Fisch? Verkäufer: Ja, direkt neben dem Fleisch. Tom: Prima, danke schön!", "unit05_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 5: Essen und Trinken ({len(unit05_vocab)} vocab + {len(unit05_sentences)} sentences + {len(unit05_dialogues)} dialogues) ===")
    for text, filename in unit05_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit05_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit05_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 6: Einkaufen
    unit06_vocab = [
        ("eins", "unit06_eins.mp3"),
        ("zwei", "unit06_zwei.mp3"),
        ("drei", "unit06_drei.mp3"),
        ("vier", "unit06_vier.mp3"),
        ("fünf", "unit06_fuenf.mp3"),
        ("sechs", "unit06_sechs.mp3"),
        ("sieben", "unit06_sieben.mp3"),
        ("acht", "unit06_acht.mp3"),
        ("neun", "unit06_neun.mp3"),
        ("zehn", "unit06_zehn.mp3"),
        ("elf", "unit06_elf.mp3"),
        ("zwölf", "unit06_zwoelf.mp3"),
        ("zwanzig", "unit06_zwanzig.mp3"),
        ("dreißig", "unit06_dreissig.mp3"),
        ("vierzig", "unit06_vierzig.mp3"),
        ("fünfzig", "unit06_fuenfzig.mp3"),
        ("hundert", "unit06_hundert.mp3"),
        ("der Euro", "unit06_euro.mp3"),
        ("der Cent", "unit06_cent.mp3"),
        ("der Preis", "unit06_preis.mp3"),
        ("kaufen", "unit06_kaufen.mp3"),
        ("verkaufen", "unit06_verkaufen.mp3"),
        ("kosten", "unit06_kosten.mp3"),
        ("bezahlen", "unit06_bezahlen.mp3"),
        ("das Geschäft", "unit06_geschaeft.mp3"),
        ("der Supermarkt", "unit06_supermarkt.mp3"),
        ("das Hemd", "unit06_hemd.mp3"),
        ("die Hose", "unit06_hose.mp3"),
        ("der Rock", "unit06_rock.mp3"),
        ("das Kleid", "unit06_kleid.mp3"),
    ]
    
    unit06_sentences = [
        ("Was kostet das?", "unit06_sent01.mp3"),
        ("Das kostet 20 Euro.", "unit06_sent02.mp3"),
        ("Ich möchte das kaufen.", "unit06_sent03.mp3"),
        ("Wo kann ich bezahlen?", "unit06_sent04.mp3"),
        ("Haben Sie eine Tüte?", "unit06_sent05.mp3"),
        ("Das ist zu teuer.", "unit06_sent06.mp3"),
        ("Ich nehme zwei Brote.", "unit06_sent07.mp3"),
        ("Brauchen Sie Hilfe?", "unit06_sent08.mp3"),
        ("Die Hose kostet 45 Euro.", "unit06_sent09.mp3"),
        ("Ich suche ein Hemd.", "unit06_sent10.mp3"),
    ]
    
    unit06_dialogues = [
        ("Im Supermarkt. Kundin: Guten Tag! Was kosten die Äpfel? Verkäufer: 2 Euro 50 pro Kilo. Kundin: Dann nehme ich 2 Kilo. Verkäufer: Gerne. Noch etwas? Kundin: Ja, eine Flasche Milch, bitte. Verkäufer: Das macht zusammen 6 Euro 50. Kundin: Hier, bitte. Verkäufer: Danke schön!", "unit06_dialog01.mp3"),
        ("Im Bekleidungsgeschäft. Verkäufer: Kann ich Ihnen helfen? Kunde: Ja, ich suche eine Hose. Verkäufer: Welche Größe haben Sie? Kunde: Größe 50. Verkäufer: Hier, diese Hose ist sehr schön. Kunde: Was kostet sie? Verkäufer: 45 Euro. Kunde: Gut, ich nehme sie. Verkäufer: Gerne. Zahlen Sie bar oder mit Karte? Kunde: Mit Karte, bitte.", "unit06_dialog02.mp3"),
        ("Auf dem Markt. Anna: Guten Morgen! Haben Sie frische Tomaten? Händler: Ja, sehr frisch! Die sind von heute Morgen. Anna: Was kosten sie? Händler: 3 Euro pro Kilo. Anna: Dann nehme ich 2 Kilo. Und diese Bananen? Händler: Die kosten 2 Euro pro Kilo. Anna: Ok, ich nehme auch 1 Kilo Bananen. Händler: Das macht 8 Euro. Anna: Bitte schön. Händler: Vielen Dank!", "unit06_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 6: Einkaufen ({len(unit06_vocab)} vocab + {len(unit06_sentences)} sentences + {len(unit06_dialogues)} dialogues) ===")
    for text, filename in unit06_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit06_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit06_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    print(f"\n✅ All audio files generated!")
    print(f"Total files: {len(unit05_vocab) + len(unit05_sentences) + len(unit05_dialogues) + len(unit06_vocab) + len(unit06_sentences) + len(unit06_dialogues)}")

if __name__ == "__main__":
    print("Starting audio generation for Units 5-6...")
    asyncio.run(generate_all())
    print("\nDone!")
