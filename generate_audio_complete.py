#!/usr/bin/env python3
"""
Complete Audio Generator for German A1 Textbook
Generates all audio files for Units 1-4
"""
import asyncio
import edge_tts
import os
from pathlib import Path

# German voice (female, clear for learning)
VOICE = "de-DE-KatjaNeural"
# Slow rate for A1 learners (-20% speed)
RATE = "-20%"

async def generate_single_audio(text, output_file):
    """Generate a single audio file"""
    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(str(output_path))
        print(f"✅ {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error: {output_file} - {e}")
        return False

async def generate_all():
    """Generate ALL audio files for the textbook"""
    
    all_audio = []
    
    # ========== UNIT 2: Familie und Freunde ==========
    print("\n📝 Unit 2: Familie und Freunde")
    unit2 = [
        # Vocabulary
        ("die Familie", "audio/vocab/familie.mp3"),
        ("die Eltern", "audio/vocab/eltern.mp3"),
        ("der Vater", "audio/vocab/vater.mp3"),
        ("die Mutter", "audio/vocab/mutter.mp3"),
        ("der Bruder", "audio/vocab/bruder.mp3"),
        ("die Schwester", "audio/vocab/schwester.mp3"),
        ("die Geschwister", "audio/vocab/geschwister.mp3"),
        ("der Sohn", "audio/vocab/sohn.mp3"),
        ("die Tochter", "audio/vocab/tochter.mp3"),
        ("das Kind", "audio/vocab/kind.mp3"),
        ("die Kinder", "audio/vocab/kinder.mp3"),
        ("der Großvater", "audio/vocab/grossvater.mp3"),
        ("die Großmutter", "audio/vocab/grossmutter.mp3"),
        ("der Freund", "audio/vocab/freund.mp3"),
        ("die Freundin", "audio/vocab/freundin.mp3"),
        ("der Mann", "audio/vocab/mann.mp3"),
        ("die Frau", "audio/vocab/frau.mp3"),
        ("verheiratet", "audio/vocab/verheiratet.mp3"),
        ("ledig", "audio/vocab/ledig.mp3"),
        ("geschieden", "audio/vocab/geschieden.mp3"),
        
        # Sentences
        ("Das ist meine Familie.", "audio/sentences/das_ist_meine_familie.mp3"),
        ("Mein Vater heißt Thomas.", "audio/sentences/mein_vater_heisst_thomas.mp3"),
        ("Meine Mutter ist 45 Jahre alt.", "audio/sentences/meine_mutter_ist_45.mp3"),
        ("Ich habe einen Bruder und eine Schwester.", "audio/sentences/ich_habe_bruder_schwester.mp3"),
        ("Sein Bruder wohnt in Berlin.", "audio/sentences/sein_bruder_wohnt_berlin.mp3"),
        ("Ihre Schwester ist Lehrerin.", "audio/sentences/ihre_schwester_lehrerin.mp3"),
        ("Unsere Kinder sind 5 und 8 Jahre alt.", "audio/sentences/unsere_kinder_5_8.mp3"),
        ("Dein Vater ist sehr nett.", "audio/sentences/dein_vater_nett.mp3"),
        ("Meine Großeltern leben in Hamburg.", "audio/sentences/grosseltern_hamburg.mp3"),
        ("Ich bin verheiratet und habe zwei Kinder.", "audio/sentences/verheiratet_zwei_kinder.mp3"),
        ("Er ist ledig und hat keine Kinder.", "audio/sentences/ledig_keine_kinder.mp3"),
        ("Meine Freundin heißt Anna.", "audio/sentences/freundin_anna.mp3"),
        
        # Dialogues
        ("Hallo! Das ist meine Familie.", "audio/dialogues/d2_01.mp3"),
        ("Mein Vater heißt Peter. Er ist 50 Jahre alt.", "audio/dialogues/d2_02.mp3"),
        ("Meine Mutter heißt Maria. Sie ist 48 Jahre alt.", "audio/dialogues/d2_03.mp3"),
        ("Ich habe einen Bruder. Sein Name ist Tom.", "audio/dialogues/d2_04.mp3"),
        ("Tom ist 22 Jahre alt. Er studiert in München.", "audio/dialogues/d2_05.mp3"),
        ("Hast du Geschwister, Max?", "audio/dialogues/d2_06.mp3"),
        ("Ja, ich habe eine Schwester. Sie heißt Sophie.", "audio/dialogues/d2_07.mp3"),
        ("Wie alt ist sie?", "audio/dialogues/d2_08.mp3"),
        ("Sie ist 18 Jahre alt. Sie geht noch zur Schule.", "audio/dialogues/d2_09.mp3"),
        ("Und deine Eltern? Was machen sie?", "audio/dialogues/d2_10.mp3"),
        ("Mein Vater ist Arzt. Meine Mutter ist Lehrerin.", "audio/dialogues/d2_11.mp3"),
        ("Bist du verheiratet, Julia?", "audio/dialogues/d2_12.mp3"),
        ("Ja, ich bin verheiratet. Mein Mann heißt Michael.", "audio/dialogues/d2_13.mp3"),
        ("Habt ihr Kinder?", "audio/dialogues/d2_14.mp3"),
        ("Ja, wir haben zwei Kinder. Einen Sohn und eine Tochter.", "audio/dialogues/d2_15.mp3"),
        ("Wie alt sind deine Kinder?", "audio/dialogues/d2_16.mp3"),
        ("Mein Sohn ist 7 und meine Tochter ist 4 Jahre alt.", "audio/dialogues/d2_17.mp3"),
    ]
    all_audio.extend(unit2)
    
    # ========== UNIT 3: Berufe und Arbeit ==========
    print("\n📝 Unit 3: Berufe und Arbeit")
    unit3 = [
        # Vocabulary
        ("der Beruf", "audio/vocab/beruf.mp3"),
        ("der Arzt", "audio/vocab/arzt.mp3"),
        ("der Lehrer", "audio/vocab/lehrer.mp3"),
        ("der Ingenieur", "audio/vocab/ingenieur.mp3"),
        ("die Krankenschwester", "audio/vocab/krankenschwester.mp3"),
        ("der Koch", "audio/vocab/koch.mp3"),
        ("der Verkäufer", "audio/vocab/verkaeufer.mp3"),
        ("der Kellner", "audio/vocab/kellner.mp3"),
        ("der Mechaniker", "audio/vocab/mechaniker.mp3"),
        ("der Polizist", "audio/vocab/polizist.mp3"),
        ("der Friseur", "audio/vocab/friseur.mp3"),
        ("der Student", "audio/vocab/student.mp3"),
        ("der Anwalt", "audio/vocab/anwalt.mp3"),
        ("der Programmierer", "audio/vocab/programmierer.mp3"),
        ("arbeiten", "audio/vocab/arbeiten.mp3"),
        ("studieren", "audio/vocab/studieren.mp3"),
        ("lernen", "audio/vocab/lernen.mp3"),
        ("verdienen", "audio/vocab/verdienen.mp3"),
        ("die Firma", "audio/vocab/firma.mp3"),
        ("das Büro", "audio/vocab/buero.mp3"),
        
        # Sentences
        ("Was bist du von Beruf?", "audio/sentences/was_bist_du_beruf.mp3"),
        ("Ich bin Lehrer von Beruf.", "audio/sentences/ich_bin_lehrer.mp3"),
        ("Sie ist Ärztin.", "audio/sentences/sie_ist_aerztin.mp3"),
        ("Ich arbeite bei einer Firma.", "audio/sentences/ich_arbeite_firma.mp3"),
        ("Er studiert Medizin.", "audio/sentences/er_studiert_medizin.mp3"),
        ("Wir arbeiten im Büro.", "audio/sentences/wir_arbeiten_buero.mp3"),
        ("Mein Vater ist Ingenieur.", "audio/sentences/vater_ingenieur.mp3"),
        ("Sie arbeitet als Krankenschwester.", "audio/sentences/krankenschwester.mp3"),
        ("Ich studiere Informatik an der Universität.", "audio/sentences/studiere_informatik.mp3"),
        ("Was machst du beruflich?", "audio/sentences/was_machst_beruflich.mp3"),
        ("Ich lerne Deutsch.", "audio/sentences/lerne_deutsch.mp3"),
        ("Er verdient viel Geld.", "audio/sentences/verdient_geld.mp3"),
        
        # Dialogues
        ("Hallo! Ich bin Anna. Was machst du beruflich?", "audio/dialogues/d3_01.mp3"),
        ("Ich bin Arzt. Ich arbeite im Krankenhaus.", "audio/dialogues/d3_02.mp3"),
        ("Interessant! Und wo ist das Krankenhaus?", "audio/dialogues/d3_03.mp3"),
        ("In Berlin. Und was bist du von Beruf?", "audio/dialogues/d3_04.mp3"),
        ("Ich bin Lehrerin. Ich unterrichte Englisch.", "audio/dialogues/d3_05.mp3"),
        ("Hallo Max! Arbeitest du schon?", "audio/dialogues/d3_06.mp3"),
        ("Nein, ich studiere noch. Ich bin Student.", "audio/dialogues/d3_07.mp3"),
        ("Was studierst du?", "audio/dialogues/d3_08.mp3"),
        ("Ich studiere Informatik. Und du?", "audio/dialogues/d3_09.mp3"),
        ("Ich arbeite als Programmiererin bei einer IT-Firma.", "audio/dialogues/d3_10.mp3"),
        ("Cool! Gefällt dir die Arbeit?", "audio/dialogues/d3_11.mp3"),
        ("Ja, sehr. Die Arbeit ist interessant.", "audio/dialogues/d3_12.mp3"),
        ("Entschuldigung, arbeiten Sie hier?", "audio/dialogues/d3_13.mp3"),
        ("Ja, ich bin Kellnerin. Was möchten Sie?", "audio/dialogues/d3_14.mp3"),
        ("Einen Kaffee, bitte.", "audio/dialogues/d3_15.mp3"),
        ("Gerne. Einen Moment, bitte.", "audio/dialogues/d3_16.mp3"),
    ]
    all_audio.extend(unit3)
    
    # ========== UNIT 4: Wohnen ==========
    print("\n📝 Unit 4: Wohnen")
    unit4 = [
        # Vocabulary
        ("die Wohnung", "audio/vocab/wohnung.mp3"),
        ("das Haus", "audio/vocab/haus.mp3"),
        ("das Zimmer", "audio/vocab/zimmer.mp3"),
        ("das Wohnzimmer", "audio/vocab/wohnzimmer.mp3"),
        ("das Schlafzimmer", "audio/vocab/schlafzimmer.mp3"),
        ("die Küche", "audio/vocab/kueche.mp3"),
        ("das Badezimmer", "audio/vocab/badezimmer.mp3"),
        ("der Balkon", "audio/vocab/balkon.mp3"),
        ("der Garten", "audio/vocab/garten.mp3"),
        ("das Sofa", "audio/vocab/sofa.mp3"),
        ("der Tisch", "audio/vocab/tisch.mp3"),
        ("der Stuhl", "audio/vocab/stuhl.mp3"),
        ("das Bett", "audio/vocab/bett.mp3"),
        ("der Schrank", "audio/vocab/schrank.mp3"),
        ("die Lampe", "audio/vocab/lampe.mp3"),
        ("der Kühlschrank", "audio/vocab/kuehlschrank.mp3"),
        ("der Herd", "audio/vocab/herd.mp3"),
        ("das Fenster", "audio/vocab/fenster.mp3"),
        ("die Tür", "audio/vocab/tuer.mp3"),
        ("die Miete", "audio/vocab/miete.mp3"),
        
        # Sentences
        ("Ich wohne in einer Wohnung.", "audio/sentences/wohne_wohnung.mp3"),
        ("Die Wohnung hat drei Zimmer.", "audio/sentences/wohnung_drei_zimmer.mp3"),
        ("Das Wohnzimmer ist groß.", "audio/sentences/wohnzimmer_gross.mp3"),
        ("Im Schlafzimmer ist ein Bett.", "audio/sentences/schlafzimmer_bett.mp3"),
        ("Die Küche ist klein aber modern.", "audio/sentences/kueche_klein_modern.mp3"),
        ("Wir haben einen Balkon.", "audio/sentences/haben_balkon.mp3"),
        ("Das Haus hat einen Garten.", "audio/sentences/haus_garten.mp3"),
        ("Im Wohnzimmer steht ein Sofa.", "audio/sentences/wohnzimmer_sofa.mp3"),
        ("Die Miete kostet 800 Euro.", "audio/sentences/miete_800_euro.mp3"),
        ("Wo wohnst du?", "audio/sentences/wo_wohnst_du.mp3"),
        
        # Dialogues
        ("Guten Tag! Ich suche eine Wohnung.", "audio/dialogues/d4_01.mp3"),
        ("Wie viele Zimmer möchten Sie?", "audio/dialogues/d4_02.mp3"),
        ("Zwei Zimmer, eine Küche und ein Bad.", "audio/dialogues/d4_03.mp3"),
        ("Möchten Sie einen Balkon?", "audio/dialogues/d4_04.mp3"),
        ("Ja, gerne. Wie viel kostet die Miete?", "audio/dialogues/d4_05.mp3"),
        ("750 Euro pro Monat.", "audio/dialogues/d4_06.mp3"),
        ("Wie ist deine neue Wohnung?", "audio/dialogues/d4_07.mp3"),
        ("Sehr schön! Sie hat drei Zimmer.", "audio/dialogues/d4_08.mp3"),
        ("Hast du auch einen Balkon?", "audio/dialogues/d4_09.mp3"),
        ("Ja, der Balkon ist groß. Und die Küche ist modern.", "audio/dialogues/d4_10.mp3"),
        ("Super! Wann ziehst du ein?", "audio/dialogues/d4_11.mp3"),
        ("Nächste Woche.", "audio/dialogues/d4_12.mp3"),
    ]
    all_audio.extend(unit4)
    
    # Generate all files
    print(f"\n🎵 Total files to generate: {len(all_audio)}")
    print("⏳ Starting generation...\n")
    
    success = 0
    failed = 0
    
    for text, filepath in all_audio:
        result = await generate_single_audio(text, filepath)
        if result:
            success += 1
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Success: {success}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(all_audio)}")
    print(f"{'='*60}")

async def main():
    print("="*60)
    print("🎙️  German A1 Textbook - Complete Audio Generator")
    print("="*60)
    print(f"Voice: {VOICE}")
    print(f"Speed: {RATE}")
    print("="*60)
    
    await generate_all()
    
    print("\n✅ Generation complete!")
    print("Run this script to generate audio files:")
    print("  python generate_audio_complete.py")

if __name__ == "__main__":
    asyncio.run(main())