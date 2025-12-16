#!/usr/bin/env python3
"""
Generate German audio files for Units 10-14 using edge-tts
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
    """Generate all audio files for Units 10-14"""
    
    # Unit 10: Reisen und Verkehr
    unit10_vocab = [
        ("der Bus", "unit10_bus.mp3"),
        ("der Zug", "unit10_zug.mp3"),
        ("das Auto", "unit10_auto.mp3"),
        ("das Fahrrad", "unit10_fahrrad.mp3"),
        ("das Flugzeug", "unit10_flugzeug.mp3"),
        ("die U-Bahn", "unit10_ubahn.mp3"),
        ("die Straßenbahn", "unit10_strassenbahn.mp3"),
        ("das Taxi", "unit10_taxi.mp3"),
        ("zu Fuß", "unit10_zu_fuss.mp3"),
        ("der Bahnhof", "unit10_bahnhof.mp3"),
        ("der Flughafen", "unit10_flughafen.mp3"),
        ("die Haltestelle", "unit10_haltestelle.mp3"),
        ("das Ticket", "unit10_ticket.mp3"),
        ("die Fahrkarte", "unit10_fahrkarte.mp3"),
        ("die Reise", "unit10_reise.mp3"),
        ("reisen", "unit10_reisen.mp3"),
        ("fahren", "unit10_fahren.mp3"),
        ("fliegen", "unit10_fliegen.mp3"),
        ("abfahren", "unit10_abfahren.mp3"),
        ("ankommen", "unit10_ankommen.mp3"),
        ("umsteigen", "unit10_umsteigen.mp3"),
        ("wollen", "unit10_wollen.mp3"),
        ("links", "unit10_links.mp3"),
        ("rechts", "unit10_rechts.mp3"),
        ("geradeaus", "unit10_geradeaus.mp3"),
    ]
    
    unit10_sentences = [
        ("Wie komme ich zum Bahnhof?", "unit10_sent01.mp3"),
        ("Ich will nach Berlin fahren.", "unit10_sent02.mp3"),
        ("Der Zug fährt um 10 Uhr ab.", "unit10_sent03.mp3"),
        ("Wann kommt der Bus an?", "unit10_sent04.mp3"),
        ("Ich fahre mit dem Auto.", "unit10_sent05.mp3"),
        ("Wo ist die Haltestelle?", "unit10_sent06.mp3"),
        ("Ich muss umsteigen.", "unit10_sent07.mp3"),
        ("Gehen Sie geradeaus!", "unit10_sent08.mp3"),
        ("Dann links abbiegen.", "unit10_sent09.mp3"),
        ("Ich fliege nach Deutschland.", "unit10_sent10.mp3"),
        ("Das Flugzeug startet um 14 Uhr.", "unit10_sent11.mp3"),
        ("Eine Fahrkarte nach München, bitte.", "unit10_sent12.mp3"),
    ]
    
    unit10_dialogues = [
        ("Am Bahnhof. Tourist: Entschuldigung, wie komme ich zum Hotel Adler? Person: Nehmen Sie die U-Bahn Linie 3. Tourist: Wo ist die U-Bahn? Person: Dort drüben, gehen Sie geradeaus und dann links. Tourist: Danke schön! Person: Bitte, gute Reise!", "unit10_dialog01.mp3"),
        ("Fahrkarte kaufen. Kunde: Guten Tag! Eine Fahrkarte nach Hamburg, bitte. Mitarbeiter: Einfach oder hin und zurück? Kunde: Hin und zurück, bitte. Mitarbeiter: Das kostet 80 Euro. Wann wollen Sie fahren? Kunde: Morgen um 9 Uhr. Mitarbeiter: Gut, hier ist Ihre Fahrkarte. Der Zug fährt von Gleis 7 ab. Kunde: Vielen Dank!", "unit10_dialog02.mp3"),
        ("Weg fragen. Person 1: Entschuldigung, wo ist der Flughafen? Person 2: Das ist weit. Sie müssen den Bus nehmen. Person 1: Welchen Bus? Person 2: Bus Nummer 100. Die Haltestelle ist dort. Person 1: Wie lange dauert die Fahrt? Person 2: Ungefähr 30 Minuten. Person 1: Danke für die Hilfe!", "unit10_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 10: Reisen und Verkehr ({len(unit10_vocab)} vocab + {len(unit10_sentences)} sentences + {len(unit10_dialogues)} dialogues) ===")
    for text, filename in unit10_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit10_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit10_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 11: Schule und Lernen
    unit11_vocab = [
        ("das Buch", "unit11_buch.mp3"),
        ("das Heft", "unit11_heft.mp3"),
        ("der Stift", "unit11_stift.mp3"),
        ("der Bleistift", "unit11_bleistift.mp3"),
        ("der Radiergummi", "unit11_radiergummi.mp3"),
        ("das Lineal", "unit11_lineal.mp3"),
        ("die Tasche", "unit11_tasche.mp3"),
        ("der Rucksack", "unit11_rucksack.mp3"),
        ("Mathematik", "unit11_mathematik.mp3"),
        ("Deutsch", "unit11_deutsch.mp3"),
        ("Englisch", "unit11_englisch.mp3"),
        ("Geschichte", "unit11_geschichte.mp3"),
        ("Biologie", "unit11_biologie.mp3"),
        ("Sport", "unit11_sport.mp3"),
        ("lernen", "unit11_lernen.mp3"),
        ("schreiben", "unit11_schreiben.mp3"),
        ("lesen", "unit11_lesen.mp3"),
        ("verstehen", "unit11_verstehen.mp3"),
        ("wiederholen", "unit11_wiederholen.mp3"),
        ("üben", "unit11_ueben.mp3"),
        ("dürfen", "unit11_duerfen.mp3"),
    ]
    
    unit11_sentences = [
        ("Ich lerne Deutsch.", "unit11_sent01.mp3"),
        ("Darf ich zur Toilette gehen?", "unit11_sent02.mp3"),
        ("Ich habe eine Frage.", "unit11_sent03.mp3"),
        ("Wir schreiben einen Test.", "unit11_sent04.mp3"),
        ("Ich habe das Buch gelesen.", "unit11_sent05.mp3"),
        ("Verstehst du die Aufgabe?", "unit11_sent06.mp3"),
    ]
    
    unit11_dialogues = [
        ("Im Unterricht. Lehrer: Guten Morgen! Heute lernen wir neue Vokabeln. Schüler: Darf ich eine Frage stellen? Lehrer: Ja, natürlich! Schüler: Ich verstehe das Wort nicht. Lehrer: Kein Problem, ich erkläre es noch einmal. Wiederholen Sie bitte!", "unit11_dialog01.mp3"),
        ("Hausaufgaben. Mutter: Hast du deine Hausaufgaben gemacht? Kind: Ja, ich habe Mathe und Deutsch gelernt. Mutter: Sehr gut! Und hast du auch gelesen? Kind: Ja, ich habe ein Buch gelesen. Mutter: Prima! Du darfst jetzt spielen.", "unit11_dialog02.mp3"),
        ("In der Bibliothek. Schüler 1: Hast du einen Stift? Schüler 2: Ja, hier bitte. Schüler 1: Danke! Was lernst du? Schüler 2: Ich lerne Englisch. Und du? Schüler 1: Ich muss Geschichte wiederholen. Schüler 2: Viel Erfolg!", "unit11_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 11: Schule und Lernen ({len(unit11_vocab)} vocab + {len(unit11_sentences)} sentences + {len(unit11_dialogues)} dialogues) ===")
    for text, filename in unit11_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit11_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit11_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 12: Medien und Kommunikation
    unit12_vocab = [
        ("das Handy", "unit12_handy.mp3"),
        ("das Smartphone", "unit12_smartphone.mp3"),
        ("der Computer", "unit12_computer.mp3"),
        ("das Tablet", "unit12_tablet.mp3"),
        ("das Internet", "unit12_internet.mp3"),
        ("die E-Mail", "unit12_email.mp3"),
        ("die SMS", "unit12_sms.mp3"),
        ("das Fernsehen", "unit12_fernsehen.mp3"),
        ("das Radio", "unit12_radio.mp3"),
        ("die Zeitung", "unit12_zeitung.mp3"),
        ("das Buch", "unit12_buch.mp3"),
        ("der Film", "unit12_film.mp3"),
        ("telefonieren", "unit12_telefonieren.mp3"),
        ("chatten", "unit12_chatten.mp3"),
        ("simsen", "unit12_simsen.mp3"),
        ("mailen", "unit12_mailen.mp3"),
        ("surfen", "unit12_surfen.mp3"),
        ("posten", "unit12_posten.mp3"),
    ]
    
    unit12_sentences = [
        ("Ich telefoniere mit meiner Mutter.", "unit12_sent01.mp3"),
        ("Ich chatte gern mit Freunden, weil es Spaß macht.", "unit12_sent02.mp3"),
        ("Ich weiß, dass du ein Smartphone hast.", "unit12_sent03.mp3"),
        ("Wenn ich Zeit habe, surfe ich im Internet.", "unit12_sent04.mp3"),
        ("Schreib mir eine E-Mail!", "unit12_sent05.mp3"),
        ("Lies die Zeitung!", "unit12_sent06.mp3"),
    ]
    
    unit12_dialogues = [
        ("Am Telefon. Anna: Hallo Tom! Tom: Hi Anna! Wie geht's? Anna: Gut, danke! Was machst du? Tom: Ich surfe gerade im Internet. Anna: Cool! Schreib mir später eine E-Mail! Tom: Ok, mache ich!", "unit12_dialog01.mp3"),
        ("Social Media. Lisa: Chattest du viel? Ben: Ja, ich chatte jeden Tag mit Freunden. Lisa: Ich auch! Ich poste auch oft Fotos. Ben: Das mache ich auch gern. Lisa: Hast du Instagram? Ben: Ja, klar! Folge mir!", "unit12_dialog02.mp3"),
        ("Medien. Vater: Was siehst du im Fernsehen? Kind: Einen Film. Vater: Welchen Film? Kind: Einen Kinderfilm. Er ist sehr lustig! Vater: Schön! Aber nicht zu lange, du musst noch lernen. Kind: Ok, Papa!", "unit12_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 12: Medien und Kommunikation ({len(unit12_vocab)} vocab + {len(unit12_sentences)} sentences + {len(unit12_dialogues)} dialogues) ===")
    for text, filename in unit12_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit12_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit12_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 13: Kultur und Feste
    unit13_vocab = [
        ("Weihnachten", "unit13_weihnachten.mp3"),
        ("Ostern", "unit13_ostern.mp3"),
        ("Neujahr", "unit13_neujahr.mp3"),
        ("Geburtstag", "unit13_geburtstag.mp3"),
        ("das Fest", "unit13_fest.mp3"),
        ("die Party", "unit13_party.mp3"),
        ("das Oktoberfest", "unit13_oktoberfest.mp3"),
        ("Karneval", "unit13_karneval.mp3"),
        ("das Geschenk", "unit13_geschenk.mp3"),
        ("die Torte", "unit13_torte.mp3"),
        ("die Kerze", "unit13_kerze.mp3"),
        ("der Weihnachtsbaum", "unit13_weihnachtsbaum.mp3"),
        ("das Feuerwerk", "unit13_feuerwerk.mp3"),
        ("die Tradition", "unit13_tradition.mp3"),
        ("feiern", "unit13_feiern.mp3"),
        ("schenken", "unit13_schenken.mp3"),
        ("gratulieren", "unit13_gratulieren.mp3"),
        ("einladen", "unit13_einladen.mp3"),
        ("singen", "unit13_singen.mp3"),
        ("tanzen", "unit13_tanzen.mp3"),
    ]
    
    unit13_sentences = [
        ("Wann ist dein Geburtstag?", "unit13_sent01.mp3"),
        ("Am 15. Mai habe ich Geburtstag.", "unit13_sent02.mp3"),
        ("Wir feiern Weihnachten im Dezember.", "unit13_sent03.mp3"),
        ("Zu Ostern suchen wir Eier.", "unit13_sent04.mp3"),
        ("Herzlichen Glückwunsch zum Geburtstag!", "unit13_sent05.mp3"),
        ("Was schenkst du ihr?", "unit13_sent06.mp3"),
    ]
    
    unit13_dialogues = [
        ("Geburtstagsfeier. Lisa: Kommst du zu meiner Geburtstagsparty? Tom: Ja, gerne! Wann ist sie? Lisa: Am Samstag um 15 Uhr. Tom: Super! Was soll ich mitbringen? Lisa: Nichts, komm einfach! Tom: Ok! Was wünschst du dir? Lisa: Überrasch mich!", "unit13_dialog01.mp3"),
        ("Weihnachten. Kind: Wann kommt der Weihnachtsmann? Mutter: Am 24. Dezember. Kind: Was bekomme ich? Mutter: Das ist eine Überraschung! Kind: Ich bin so aufgeregt! Mutter: Wir schmücken morgen den Weihnachtsbaum. Kind: Toll!", "unit13_dialog02.mp3"),
        ("Neujahr. Anna: Frohes neues Jahr! Ben: Dir auch! Hast du gute Vorsätze? Anna: Ja, ich will mehr Sport machen. Ben: Ich auch! Und ich will Deutsch lernen. Anna: Das ist ein guter Vorsatz! Ben: Danke! Prost Neujahr!", "unit13_dialog03.mp3"),
    ]
    
    print(f"\n=== Unit 13: Kultur und Feste ({len(unit13_vocab)} vocab + {len(unit13_sentences)} sentences + {len(unit13_dialogues)} dialogues) ===")
    for text, filename in unit13_vocab:
        await generate_audio(text, filename, "vocab")
    for text, filename in unit13_sentences:
        await generate_audio(text, filename, "sentences")
    for text, filename in unit13_dialogues:
        await generate_audio(text, filename, "dialogues")
    
    # Unit 14: No new vocabulary (review unit)
    print(f"\n=== Unit 14: Prüfungsvorbereitung (Review unit - uses existing vocabulary) ===")
    print("No new audio files needed for Unit 14")
    
    print(f"\n✅ Units 10-13 audio files generated!")
    total = (len(unit10_vocab) + len(unit10_sentences) + len(unit10_dialogues) +
             len(unit11_vocab) + len(unit11_sentences) + len(unit11_dialogues) +
             len(unit12_vocab) + len(unit12_sentences) + len(unit12_dialogues) +
             len(unit13_vocab) + len(unit13_sentences) + len(unit13_dialogues))
    print(f"Total files: {total}")

if __name__ == "__main__":
    print("Starting audio generation for Units 10-13...")
    asyncio.run(generate_all())
    print("\nDone!")
