#!/usr/bin/env python3
"""
Generate all remaining audio files for Units 7-14
"""

import asyncio
import edge_tts
import os
from pathlib import Path

async def generate_audio_file(text, output_path, voice="de-DE-KatjaNeural"):
    """Generate audio file from text using edge-tts"""
    communicate = edge_tts.Communicate(text, voice, rate="-20%")
    await communicate.save(output_path)

def ensure_audio_directories():
    """Create audio directories if they don't exist"""
    base_dir = Path("audio")
    for subdir in ["vocab", "sentences", "dialogues"]:
        (base_dir / subdir).mkdir(parents=True, exist_ok=True)

async def generate_all_remaining_audio():
    """Generate all audio files for Units 7-14"""
    
    ensure_audio_directories()
    
    # Unit 7: Kleidung (Clothing)
    unit7_vocab = [
        ("die Kleidung", "audio/vocab/unit7_kleidung.mp3"),
        ("das T-Shirt", "audio/vocab/unit7_t_shirt.mp3"),
        ("die Hose", "audio/vocab/unit7_hose.mp3"),
        ("das Kleid", "audio/vocab/unit7_kleid.mp3"),
        ("der Rock", "audio/vocab/unit7_rock.mp3"),
        ("die Jacke", "audio/vocab/unit7_jacke.mp3"),
        ("der Mantel", "audio/vocab/unit7_mantel.mp3"),
        ("die Schuhe", "audio/vocab/unit7_schuhe.mp3"),
        ("die Socken", "audio/vocab/unit7_socken.mp3"),
        ("der Hut", "audio/vocab/unit7_hut.mp3"),
        ("schön", "audio/vocab/unit7_schoen.mp3"),
        ("hässlich", "audio/vocab/unit7_haesslich.mp3"),
        ("groß", "audio/vocab/unit7_gross.mp3"),
        ("klein", "audio/vocab/unit7_klein.mp3"),
        ("teuer", "audio/vocab/unit7_teuer.mp3"),
        ("billig", "audio/vocab/unit7_billig.mp3"),
        ("rot", "audio/vocab/unit7_rot.mp3"),
        ("blau", "audio/vocab/unit7_blau.mp3"),
        ("grün", "audio/vocab/unit7_gruen.mp3"),
        ("gelb", "audio/vocab/unit7_gelb.mp3")
    ]
    
    unit7_sentences = [
        ("Ich trage eine blaue Hose.", "audio/sentences/unit7_sentence1.mp3"),
        ("Das Kleid ist sehr schön.", "audio/sentences/unit7_sentence2.mp3"),
        ("Die Schuhe sind zu klein.", "audio/sentences/unit7_sentence3.mp3"),
        ("Der Mantel ist warm.", "audio/sentences/unit7_sentence4.mp3"),
        ("Welche Farbe hat dein T-Shirt?", "audio/sentences/unit7_sentence5.mp3")
    ]
    
    unit7_dialogue = [
        ("A: Entschuldigung, wo finde ich T-Shirts?", "audio/dialogues/unit7_dialogue1.mp3"),
        ("B: Die T-Shirts sind im ersten Stock.", "audio/dialogues/unit7_dialogue2.mp3"),
        ("A: Danke. Haben Sie auch Hosen?", "audio/dialogues/unit7_dialogue3.mp3"),
        ("B: Ja, die Hosen sind auch im ersten Stock.", "audio/dialogues/unit7_dialogue4.mp3")
    ]
    
    # Unit 8: Gesundheit (Health)
    unit8_vocab = [
        ("die Gesundheit", "audio/vocab/unit8_gesundheit.mp3"),
        ("krank", "audio/vocab/unit8_krank.mp3"),
        ("gesund", "audio/vocab/unit8_gesund.mp3"),
        ("der Kopf", "audio/vocab/unit8_kopf.mp3"),
        ("der Bauch", "audio/vocab/unit8_bauch.mp3"),
        ("das Bein", "audio/vocab/unit8_bein.mp3"),
        ("der Arm", "audio/vocab/unit8_arm.mp3"),
        ("die Hand", "audio/vocab/unit8_hand.mp3"),
        ("der Fuß", "audio/vocab/unit8_fuss.mp3"),
        ("die Kopfschmerzen", "audio/vocab/unit8_kopfschmerzen.mp3"),
        ("die Bauchschmerzen", "audio/vocab/unit8_bauchschmerzen.mp3"),
        ("das Fieber", "audio/vocab/unit8_fieber.mp3"),
        ("die Erkältung", "audio/vocab/unit8_erkaeltung.mp3"),
        ("der Husten", "audio/vocab/unit8_husten.mp3"),
        ("der Arzt", "audio/vocab/unit8_arzt.mp3"),
        ("die Medizin", "audio/vocab/unit8_medizin.mp3"),
        ("das Krankenhaus", "audio/vocab/unit8_krankenhaus.mp3"),
        ("die Apotheke", "audio/vocab/unit8_apotheke.mp3")
    ]
    
    unit8_sentences = [
        ("Mir tut der Kopf weh.", "audio/sentences/unit8_sentence1.mp3"),
        ("Ich bin krank.", "audio/sentences/unit8_sentence2.mp3"),
        ("Ich brauche einen Arzt.", "audio/sentences/unit8_sentence3.mp3"),
        ("Wo ist die nächste Apotheke?", "audio/sentences/unit8_sentence4.mp3"),
        ("Ich habe Fieber.", "audio/sentences/unit8_sentence5.mp3")
    ]
    
    unit8_dialogue = [
        ("A: Guten Tag, Herr Doktor.", "audio/dialogues/unit8_dialogue1.mp3"),
        ("B: Guten Tag. Was kann ich für Sie tun?", "audio/dialogues/unit8_dialogue2.mp3"),
        ("A: Mir tut der Kopf weh.", "audio/dialogues/unit8_dialogue3.mp3"),
        ("B: Haben Sie auch Fieber?", "audio/dialogues/unit8_dialogue4.mp3"),
        ("A: Ja, ein bisschen.", "audio/dialogues/unit8_dialogue5.mp3")
    ]
    
    # Unit 9: Reisen (Travel)
    unit9_vocab = [
        ("reisen", "audio/vocab/unit9_reisen.mp3"),
        ("die Reise", "audio/vocab/unit9_reise.mp3"),
        ("der Urlaub", "audio/vocab/unit9_urlaub.mp3"),
        ("das Flugzeug", "audio/vocab/unit9_flugzeug.mp3"),
        ("der Zug", "audio/vocab/unit9_zug.mp3"),
        ("das Auto", "audio/vocab/unit9_auto.mp3"),
        ("der Bus", "audio/vocab/unit9_bus.mp3"),
        ("das Taxi", "audio/vocab/unit9_taxi.mp3"),
        ("das Hotel", "audio/vocab/unit9_hotel.mp3"),
        ("die Pension", "audio/vocab/unit9_pension.mp3"),
        ("der Bahnhof", "audio/vocab/unit9_bahnhof.mp3"),
        ("der Flughafen", "audio/vocab/unit9_flughafen.mp3"),
        ("das Ticket", "audio/vocab/unit9_ticket.mp3"),
        ("die Fahrkarte", "audio/vocab/unit9_fahrkarte.mp3"),
        ("der Koffer", "audio/vocab/unit9_koffer.mp3"),
        ("das Gepäck", "audio/vocab/unit9_gepaeck.mp3"),
        ("der Pass", "audio/vocab/unit9_pass.mp3"),
        ("das Visum", "audio/vocab/unit9_visum.mp3")
    ]
    
    unit9_sentences = [
        ("Ich fahre nach Berlin.", "audio/sentences/unit9_sentence1.mp3"),
        ("Wann fährt der Zug ab?", "audio/sentences/unit9_sentence2.mp3"),
        ("Ich möchte ein Ticket nach München.", "audio/sentences/unit9_sentence3.mp3"),
        ("Wo ist mein Gepäck?", "audio/sentences/unit9_sentence4.mp3"),
        ("Das Hotel ist sehr schön.", "audio/sentences/unit9_sentence5.mp3")
    ]
    
    unit9_dialogue = [
        ("A: Eine Fahrkarte nach Hamburg, bitte.", "audio/dialogues/unit9_dialogue1.mp3"),
        ("B: Einfach oder hin und zurück?", "audio/dialogues/unit9_dialogue2.mp3"),
        ("A: Hin und zurück, bitte.", "audio/dialogues/unit9_dialogue3.mp3"),
        ("B: Das macht 45 Euro.", "audio/dialogues/unit9_dialogue4.mp3")
    ]
    
    # Unit 10: Wetter (Weather)
    unit10_vocab = [
        ("das Wetter", "audio/vocab/unit10_wetter.mp3"),
        ("die Sonne", "audio/vocab/unit10_sonne.mp3"),
        ("der Regen", "audio/vocab/unit10_regen.mp3"),
        ("der Schnee", "audio/vocab/unit10_schnee.mp3"),
        ("der Wind", "audio/vocab/unit10_wind.mp3"),
        ("die Wolke", "audio/vocab/unit10_wolke.mp3"),
        ("warm", "audio/vocab/unit10_warm.mp3"),
        ("kalt", "audio/vocab/unit10_kalt.mp3"),
        ("heiß", "audio/vocab/unit10_heiss.mp3"),
        ("kühl", "audio/vocab/unit10_kuehl.mp3"),
        ("sonnig", "audio/vocab/unit10_sonnig.mp3"),
        ("regnerisch", "audio/vocab/unit10_regnerisch.mp3"),
        ("bewölkt", "audio/vocab/unit10_bewoelkt.mp3"),
        ("windig", "audio/vocab/unit10_windig.mp3"),
        ("der Grad", "audio/vocab/unit10_grad.mp3"),
        ("die Temperatur", "audio/vocab/unit10_temperatur.mp3")
    ]
    
    unit10_sentences = [
        ("Wie ist das Wetter heute?", "audio/sentences/unit10_sentence1.mp3"),
        ("Es ist sonnig und warm.", "audio/sentences/unit10_sentence2.mp3"),
        ("Es regnet.", "audio/sentences/unit10_sentence3.mp3"),
        ("Es ist sehr kalt.", "audio/sentences/unit10_sentence4.mp3"),
        ("Die Temperatur ist 20 Grad.", "audio/sentences/unit10_sentence5.mp3")
    ]
    
    unit10_dialogue = [
        ("A: Wie ist das Wetter morgen?", "audio/dialogues/unit10_dialogue1.mp3"),
        ("B: Es wird regnen.", "audio/dialogues/unit10_dialogue2.mp3"),
        ("A: Schade. Ich wollte spazieren gehen.", "audio/dialogues/unit10_dialogue3.mp3"),
        ("B: Am Sonntag wird es wieder sonnig.", "audio/dialogues/unit10_dialogue4.mp3")
    ]
    
    # Unit 11: Zeit und Termine (Time and Appointments)
    unit11_vocab = [
        ("die Zeit", "audio/vocab/unit11_zeit.mp3"),
        ("der Termin", "audio/vocab/unit11_termin.mp3"),
        ("früh", "audio/vocab/unit11_frueh.mp3"),
        ("spät", "audio/vocab/unit11_spaet.mp3"),
        ("pünktlich", "audio/vocab/unit11_puenktlich.mp3"),
        ("heute", "audio/vocab/unit11_heute.mp3"),
        ("morgen", "audio/vocab/unit11_morgen.mp3"),
        ("gestern", "audio/vocab/unit11_gestern.mp3"),
        ("der Montag", "audio/vocab/unit11_montag.mp3"),
        ("der Dienstag", "audio/vocab/unit11_dienstag.mp3"),
        ("der Mittwoch", "audio/vocab/unit11_mittwoch.mp3"),
        ("der Donnerstag", "audio/vocab/unit11_donnerstag.mp3"),
        ("der Freitag", "audio/vocab/unit11_freitag.mp3"),
        ("der Samstag", "audio/vocab/unit11_samstag.mp3"),
        ("der Sonntag", "audio/vocab/unit11_sonntag.mp3"),
        ("der Januar", "audio/vocab/unit11_januar.mp3"),
        ("der Februar", "audio/vocab/unit11_februar.mp3"),
        ("der März", "audio/vocab/unit11_maerz.mp3")
    ]
    
    unit11_sentences = [
        ("Wie spät ist es?", "audio/sentences/unit11_sentence1.mp3"),
        ("Es ist acht Uhr.", "audio/sentences/unit11_sentence2.mp3"),
        ("Ich habe einen Termin.", "audio/sentences/unit11_sentence3.mp3"),
        ("Wann treffen wir uns?", "audio/sentences/unit11_sentence4.mp3"),
        ("Um zehn Uhr.", "audio/sentences/unit11_sentence5.mp3")
    ]
    
    unit11_dialogue = [
        ("A: Haben Sie heute Zeit?", "audio/dialogues/unit11_dialogue1.mp3"),
        ("B: Nein, heute habe ich keine Zeit.", "audio/dialogues/unit11_dialogue2.mp3"),
        ("A: Und morgen?", "audio/dialogues/unit11_dialogue3.mp3"),
        ("B: Morgen um 14 Uhr passt es mir.", "audio/dialogues/unit11_dialogue4.mp3")
    ]
    
    # Unit 12: Arbeit (Work)
    unit12_vocab = [
        ("die Arbeit", "audio/vocab/unit12_arbeit.mp3"),
        ("arbeiten", "audio/vocab/unit12_arbeiten.mp3"),
        ("der Job", "audio/vocab/unit12_job.mp3"),
        ("der Beruf", "audio/vocab/unit12_beruf.mp3"),
        ("das Büro", "audio/vocab/unit12_buero.mp3"),
        ("der Chef", "audio/vocab/unit12_chef.mp3"),
        ("der Kollege", "audio/vocab/unit12_kollege.mp3"),
        ("die Kollegin", "audio/vocab/unit12_kollegin.mp3"),
        ("der Lehrer", "audio/vocab/unit12_lehrer.mp3"),
        ("der Arzt", "audio/vocab/unit12_arzt.mp3"),
        ("der Verkäufer", "audio/vocab/unit12_verkaeufer.mp3"),
        ("der Student", "audio/vocab/unit12_student.mp3"),
        ("das Geld", "audio/vocab/unit12_geld.mp3"),
        ("verdienen", "audio/vocab/unit12_verdienen.mp3"),
        ("bezahlen", "audio/vocab/unit12_bezahlen.mp3"),
        ("das Gehalt", "audio/vocab/unit12_gehalt.mp3")
    ]
    
    unit12_sentences = [
        ("Ich arbeite in einem Büro.", "audio/sentences/unit12_sentence1.mp3"),
        ("Was sind Sie von Beruf?", "audio/sentences/unit12_sentence2.mp3"),
        ("Ich bin Lehrer.", "audio/sentences/unit12_sentence3.mp3"),
        ("Wo arbeiten Sie?", "audio/sentences/unit12_sentence4.mp3"),
        ("Ich arbeite in Berlin.", "audio/sentences/unit12_sentence5.mp3")
    ]
    
    unit12_dialogue = [
        ("A: Was machen Sie beruflich?", "audio/dialogues/unit12_dialogue1.mp3"),
        ("B: Ich bin Verkäufer.", "audio/dialogues/unit12_dialogue2.mp3"),
        ("A: Gefällt Ihnen die Arbeit?", "audio/dialogues/unit12_dialogue3.mp3"),
        ("B: Ja, die Arbeit macht mir Spaß.", "audio/dialogues/unit12_dialogue4.mp3")
    ]
    
    # Unit 13: Schule und Bildung (School and Education)
    unit13_vocab = [
        ("die Schule", "audio/vocab/unit13_schule.mp3"),
        ("lernen", "audio/vocab/unit13_lernen.mp3"),
        ("studieren", "audio/vocab/unit13_studieren.mp3"),
        ("der Schüler", "audio/vocab/unit13_schueler.mp3"),
        ("die Schülerin", "audio/vocab/unit13_schuelerin.mp3"),
        ("der Student", "audio/vocab/unit13_student.mp3"),
        ("die Studentin", "audio/vocab/unit13_studentin.mp3"),
        ("das Buch", "audio/vocab/unit13_buch.mp3"),
        ("das Heft", "audio/vocab/unit13_heft.mp3"),
        ("der Stift", "audio/vocab/unit13_stift.mp3"),
        ("die Prüfung", "audio/vocab/unit13_pruefung.mp3"),
        ("die Note", "audio/vocab/unit13_note.mp3"),
        ("die Hausaufgabe", "audio/vocab/unit13_hausaufgabe.mp3"),
        ("die Universität", "audio/vocab/unit13_universitaet.mp3"),
        ("das Fach", "audio/vocab/unit13_fach.mp3"),
        ("Deutsch", "audio/vocab/unit13_deutsch.mp3"),
        ("Englisch", "audio/vocab/unit13_englisch.mp3"),
        ("Mathematik", "audio/vocab/unit13_mathematik.mp3")
    ]
    
    unit13_sentences = [
        ("Ich lerne Deutsch.", "audio/sentences/unit13_sentence1.mp3"),
        ("Gehst du zur Schule?", "audio/sentences/unit13_sentence2.mp3"),
        ("Ich studiere an der Universität.", "audio/sentences/unit13_sentence3.mp3"),
        ("Wann ist die Prüfung?", "audio/sentences/unit13_sentence4.mp3"),
        ("Ich mache meine Hausaufgaben.", "audio/sentences/unit13_sentence5.mp3")
    ]
    
    unit13_dialogue = [
        ("A: Was studierst du?", "audio/dialogues/unit13_dialogue1.mp3"),
        ("B: Ich studiere Medizin.", "audio/dialogues/unit13_dialogue2.mp3"),
        ("A: Ist das schwer?", "audio/dialogues/unit13_dialogue3.mp3"),
        ("B: Ja, aber es macht Spaß.", "audio/dialogues/unit13_dialogue4.mp3")
    ]
    
    # Unit 14: Prüfungsvorbereitung (Exam Preparation)
    unit14_vocab = [
        ("die Prüfung", "audio/vocab/unit14_pruefung.mp3"),
        ("die Vorbereitung", "audio/vocab/unit14_vorbereitung.mp3"),
        ("wiederholen", "audio/vocab/unit14_wiederholen.mp3"),
        ("üben", "audio/vocab/unit14_ueben.mp3"),
        ("schwer", "audio/vocab/unit14_schwer.mp3"),
        ("leicht", "audio/vocab/unit14_leicht.mp3"),
        ("richtig", "audio/vocab/unit14_richtig.mp3"),
        ("falsch", "audio/vocab/unit14_falsch.mp3"),
        ("die Antwort", "audio/vocab/unit14_antwort.mp3"),
        ("die Frage", "audio/vocab/unit14_frage.mp3"),
        ("das Zertifikat", "audio/vocab/unit14_zertifikat.mp3"),
        ("bestehen", "audio/vocab/unit14_bestehen.mp3"),
        ("durchfallen", "audio/vocab/unit14_durchfallen.mp3"),
        ("die Grammatik", "audio/vocab/unit14_grammatik.mp3"),
        ("der Wortschatz", "audio/vocab/unit14_wortschatz.mp3")
    ]
    
    unit14_sentences = [
        ("Ich bereite mich auf die Prüfung vor.", "audio/sentences/unit14_sentence1.mp3"),
        ("Das ist die richtige Antwort.", "audio/sentences/unit14_sentence2.mp3"),
        ("Ich muss mehr üben.", "audio/sentences/unit14_sentence3.mp3"),
        ("Die Prüfung ist schwer.", "audio/sentences/unit14_sentence4.mp3"),
        ("Ich hoffe, ich bestehe.", "audio/sentences/unit14_sentence5.mp3")
    ]
    
    unit14_dialogue = [
        ("A: Bist du bereit für die Prüfung?", "audio/dialogues/unit14_dialogue1.mp3"),
        ("B: Ich bin noch nicht sicher.", "audio/dialogues/unit14_dialogue2.mp3"),
        ("A: Hast du genug gelernt?", "audio/dialogues/unit14_dialogue3.mp3"),
        ("B: Ich glaube schon.", "audio/dialogues/unit14_dialogue4.mp3")
    ]
    
    # Combine all audio files
    all_audio = (unit7_vocab + unit7_sentences + unit7_dialogue +
                unit8_vocab + unit8_sentences + unit8_dialogue +
                unit9_vocab + unit9_sentences + unit9_dialogue +
                unit10_vocab + unit10_sentences + unit10_dialogue +
                unit11_vocab + unit11_sentences + unit11_dialogue +
                unit12_vocab + unit12_sentences + unit12_dialogue +
                unit13_vocab + unit13_sentences + unit13_dialogue +
                unit14_vocab + unit14_sentences + unit14_dialogue)
    
    print(f"Generating {len(all_audio)} audio files for Units 7-14...")
    
    for i, (text, output_path) in enumerate(all_audio, 1):
        if not os.path.exists(output_path):
            try:
                await generate_audio_file(text, output_path)
                print(f"  ✅ Generated [{i:3d}/{len(all_audio)}]: {os.path.basename(output_path)}")
            except Exception as e:
                print(f"  ❌ Failed [{i:3d}/{len(all_audio)}]: {os.path.basename(output_path)} - {e}")
        else:
            print(f"  ⏭️  Exists [{i:3d}/{len(all_audio)}]: {os.path.basename(output_path)}")
    
    print(f"\n✅ Audio generation complete! Generated {len(all_audio)} files for Units 7-14")

if __name__ == "__main__":
    asyncio.run(generate_all_remaining_audio())