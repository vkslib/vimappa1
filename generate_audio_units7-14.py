#!/usr/bin/env python3
"""
Generate German audio files for Units 7-14 using edge-tts
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
    """Generate all audio files for Units 7-14"""
    
    # Unit 7: Freizeit und Hobbys
    unit07_vocab = [
        ("das Hobby", "unit07_hobby.mp3"),
        ("die Freizeit", "unit07_freizeit.mp3"),
        ("der Sport", "unit07_sport.mp3"),
        ("Fußball spielen", "unit07_fussball_spielen.mp3"),
        ("Tennis spielen", "unit07_tennis_spielen.mp3"),
        ("schwimmen", "unit07_schwimmen.mp3"),
        ("laufen", "unit07_laufen.mp3"),
        ("Rad fahren", "unit07_rad_fahren.mp3"),
        ("tanzen", "unit07_tanzen.mp3"),
        ("wandern", "unit07_wandern.mp3"),
        ("lesen", "unit07_lesen.mp3"),
        ("Musik hören", "unit07_musik_hoeren.mp3"),
        ("singen", "unit07_singen.mp3"),
        ("malen", "unit07_malen.mp3"),
        ("fotografieren", "unit07_fotografieren.mp3"),
        ("kochen", "unit07_kochen.mp3"),
        ("das Kino", "unit07_kino.mp3"),
        ("das Theater", "unit07_theater.mp3"),
        ("das Museum", "unit07_museum.mp3"),
        ("der Park", "unit07_park.mp3"),
        ("das Schwimmbad", "unit07_schwimmbad.mp3"),
        ("die Zeit", "unit07_zeit.mp3"),
        ("haben", "unit07_haben.mp3"),
        ("gehen", "unit07_gehen.mp3"),
        ("mögen", "unit07_moegen.mp3"),
    ]
    
    unit07_sentences = [
        ("Was machst du gern?", "unit07_sent01.mp3"),
        ("Ich spiele gern Fußball.", "unit07_sent02.mp3"),
        ("Mein Hobby ist Lesen.", "unit07_sent03.mp3"),
        ("Am Wochenende gehe ich schwimmen.", "unit07_sent04.mp3"),
        ("Ich höre gern Musik.", "unit07_sent05.mp3"),
        ("Gehst du oft ins Kino?", "unit07_sent06.mp3"),
        ("Ja, ich gehe zweimal im Monat ins Kino.", "unit07_sent07.mp3"),
        ("In meiner Freizeit lese ich Bücher.", "unit07_sent08.mp3"),
        ("Wir spielen am Samstag Tennis.", "unit07_sent09.mp3"),
        ("Sie tanzt sehr gern.", "unit07_sent10.mp3"),
    ]
    
    unit07_dialogues = [
        ("Hobbys. Lisa: Hallo Tom! Was machst du gern in deiner Freizeit? Tom: Ich spiele gern Fußball. Und du? Lisa: Ich lese gern Bücher und höre Musik. Tom: Cool! Spielst du auch Sport? Lisa: Ja, ich gehe manchmal schwimmen. Tom: Prima! Vielleicht können wir zusammen schwimmen gehen?", "unit07_dialog01.mp3"),
        ("Am Wochenende. Anna: Was machst du am Wochenende? Ben: Am Samstag spiele ich Tennis. Und am Sonntag gehe ich wandern. Anna: Wandern? Wo denn? Ben: Im Park oder in den Bergen. Anna: Das klingt schön! Kann ich mitkommen? Ben: Natürlich! Wir treffen uns um 10 Uhr.", "unit07_dialog02.mp3"),
        ("Im Schwimmbad. Kind 1: Gehst du gern schwimmen? Kind 2: Ja, sehr gern! Und du? Kind 1: Ich auch! Wie oft gehst du schwimmen? Kind 2: Jeden Samstag. Kind 1: Super! Ich gehe auch jeden Samstag. Kind 2: Dann können wir zusammen schwimmen!", "unit07_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 7: Freizeit und Hobbys ({len(unit07_vocab)} vocab + {len(unit07_sentences)} sentences + {len(unit07_dialogues)} dialogues) ===")
    for text, filename in unit07_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit07_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit07_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 8: Gesundheit und Körper
    unit08_vocab = [
        ("der Kopf", "unit08_kopf.mp3"),
        ("der Hals", "unit08_hals.mp3"),
        ("der Arm", "unit08_arm.mp3"),
        ("die Hand", "unit08_hand.mp3"),
        ("der Finger", "unit08_finger.mp3"),
        ("das Bein", "unit08_bein.mp3"),
        ("der Fuß", "unit08_fuss.mp3"),
        ("der Bauch", "unit08_bauch.mp3"),
        ("der Rücken", "unit08_ruecken.mp3"),
        ("das Auge", "unit08_auge.mp3"),
        ("das Ohr", "unit08_ohr.mp3"),
        ("die Nase", "unit08_nase.mp3"),
        ("der Mund", "unit08_mund.mp3"),
        ("gesund", "unit08_gesund.mp3"),
        ("krank", "unit08_krank.mp3"),
        ("die Schmerzen", "unit08_schmerzen.mp3"),
        ("das Fieber", "unit08_fieber.mp3"),
        ("die Erkältung", "unit08_erkaeltung.mp3"),
        ("der Arzt", "unit08_arzt.mp3"),
        ("die Ärztin", "unit08_aerztin.mp3"),
        ("die Apotheke", "unit08_apotheke.mp3"),
        ("das Medikament", "unit08_medikament.mp3"),
        ("schlafen", "unit08_schlafen.mp3"),
        ("sich fühlen", "unit08_sich_fuehlen.mp3"),
        ("wehtun", "unit08_wehtun.mp3"),
    ]
    
    unit08_sentences = [
        ("Wie geht es dir?", "unit08_sent01.mp3"),
        ("Mir geht es gut.", "unit08_sent02.mp3"),
        ("Ich bin krank.", "unit08_sent03.mp3"),
        ("Mein Kopf tut weh.", "unit08_sent04.mp3"),
        ("Ich habe Fieber.", "unit08_sent05.mp3"),
        ("Ich gehe zum Arzt.", "unit08_sent06.mp3"),
        ("Nimm das Medikament!", "unit08_sent07.mp3"),
        ("Du sollst viel schlafen.", "unit08_sent08.mp3"),
        ("Gute Besserung!", "unit08_sent09.mp3"),
        ("Ich fühle mich nicht gut.", "unit08_sent10.mp3"),
    ]
    
    unit08_dialogues = [
        ("Beim Arzt. Arzt: Guten Tag! Was fehlt Ihnen? Patient: Ich fühle mich nicht gut. Ich habe Kopfschmerzen und Fieber. Arzt: Seit wann haben Sie Fieber? Patient: Seit gestern. Arzt: Ich sehe. Sie haben eine Erkältung. Nehmen Sie dieses Medikament und schlafen Sie viel. Patient: Danke, Herr Doktor!", "unit08_dialog01.mp3"),
        ("Zu Hause. Mutter: Was ist los? Bist du krank? Kind: Ja, mein Bauch tut weh. Mutter: Seit wann? Kind: Seit heute Morgen. Mutter: Hast du Fieber? Kind: Ich weiß nicht. Mutter: Komm, ich messe deine Temperatur. Du sollst im Bett bleiben. Kind: Ok, Mama.", "unit08_dialog02.mp3"),
        ("In der Apotheke. Kunde: Guten Tag! Ich habe Halsschmerzen. Haben Sie ein Medikament? Apotheker: Ja, natürlich. Nehmen Sie diese Tabletten. Kunde: Wie oft soll ich sie nehmen? Apotheker: Dreimal täglich nach dem Essen. Kunde: Danke schön! Apotheker: Gute Besserung!", "unit08_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 8: Gesundheit und Körper ({len(unit08_vocab)} vocab + {len(unit08_sentences)} sentences + {len(unit08_dialogues)} dialogues) ===")
    for text, filename in unit08_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit08_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit08_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 9: Wetter und Jahreszeiten
    unit09_vocab = [
        ("der Frühling", "unit09_fruehling.mp3"),
        ("der Sommer", "unit09_sommer.mp3"),
        ("der Herbst", "unit09_herbst.mp3"),
        ("der Winter", "unit09_winter.mp3"),
        ("Januar", "unit09_januar.mp3"),
        ("Februar", "unit09_februar.mp3"),
        ("März", "unit09_maerz.mp3"),
        ("April", "unit09_april.mp3"),
        ("Mai", "unit09_mai.mp3"),
        ("Juni", "unit09_juni.mp3"),
        ("Juli", "unit09_juli.mp3"),
        ("August", "unit09_august.mp3"),
        ("September", "unit09_september.mp3"),
        ("Oktober", "unit09_oktober.mp3"),
        ("November", "unit09_november.mp3"),
        ("Dezember", "unit09_dezember.mp3"),
        ("das Wetter", "unit09_wetter.mp3"),
        ("die Sonne", "unit09_sonne.mp3"),
        ("der Regen", "unit09_regen.mp3"),
        ("der Schnee", "unit09_schnee.mp3"),
        ("der Wind", "unit09_wind.mp3"),
        ("die Wolke", "unit09_wolke.mp3"),
        ("warm", "unit09_warm.mp3"),
        ("kalt", "unit09_kalt.mp3"),
        ("heiß", "unit09_heiss.mp3"),
        ("kühl", "unit09_kuehl.mp3"),
        ("sonnig", "unit09_sonnig.mp3"),
        ("regnerisch", "unit09_regnerisch.mp3"),
        ("bewölkt", "unit09_bewoelkt.mp3"),
        ("schneit", "unit09_schneit.mp3"),
        ("regnet", "unit09_regnet.mp3"),
        ("scheint", "unit09_scheint.mp3"),
    ]
    
    unit09_sentences = [
        ("Wie ist das Wetter heute?", "unit09_sent01.mp3"),
        ("Es ist sonnig und warm.", "unit09_sent02.mp3"),
        ("Es regnet.", "unit09_sent03.mp3"),
        ("Im Winter schneit es.", "unit09_sent04.mp3"),
        ("Die Sonne scheint.", "unit09_sent05.mp3"),
        ("Es ist sehr kalt.", "unit09_sent06.mp3"),
        ("Im Sommer ist es heiß.", "unit09_sent07.mp3"),
        ("Welche Jahreszeit magst du?", "unit09_sent08.mp3"),
        ("Ich mag den Frühling.", "unit09_sent09.mp3"),
        ("Im April regnet es oft.", "unit09_sent10.mp3"),
        ("Heute ist es bewölkt.", "unit09_sent11.mp3"),
        ("Im Dezember ist es kalt.", "unit09_sent12.mp3"),
    ]
    
    unit09_dialogues = [
        ("Wettervorhersage. Anna: Wie ist das Wetter morgen? Ben: Es wird sonnig und warm. Anna: Prima! Dann können wir in den Park gehen. Ben: Ja, gute Idee! Die Sonne soll den ganzen Tag scheinen. Anna: Super! Ich mag sonniges Wetter.", "unit09_dialog01.mp3"),
        ("Jahreszeiten. Lisa: Welche Jahreszeit magst du am liebsten? Tom: Ich mag den Sommer. Es ist warm und sonnig. Lisa: Ich mag den Herbst. Die Blätter sind so schön bunt. Tom: Ja, der Herbst ist auch schön. Aber im Sommer kann man schwimmen gehen!", "unit09_dialog02.mp3"),
        ("Im Winter. Mutter: Zieh deine Jacke an! Es ist sehr kalt draußen. Kind: Schneit es? Mutter: Ja, es schneit! Kind: Super! Kann ich einen Schneemann bauen? Mutter: Ja, aber zieh dich warm an!", "unit09_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 9: Wetter und Jahreszeiten ({len(unit09_vocab)} vocab + {len(unit09_sentences)} sentences + {len(unit09_dialogues)} dialogues) ===")
    for text, filename in unit09_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit09_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit09_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    print(f"\n✅ Units 7-9 audio files generated!")
    total = (len(unit07_vocab) + len(unit07_sentences) + len(unit07_dialogues) +
             len(unit08_vocab) + len(unit08_sentences) + len(unit08_dialogues) +
             len(unit09_vocab) + len(unit09_sentences) + len(unit09_dialogues))
    print(f"Total files: {total}")

if __name__ == "__main__":
    print("Starting audio generation for Units 7-9...")
    asyncio.run(generate_all())
    print("\nDone!")
