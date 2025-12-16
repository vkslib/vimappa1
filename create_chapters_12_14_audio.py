#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German sentences and dialogues audio files for chapters 12-14
"""
import asyncio
import edge_tts
import os

async def create_chapters_12_14_audio():
    """Create missing audio files for chapters 12-14"""
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Chapter 12 - Hotel und Reisen (Hotel and Travel)
    ch12_data = {
        "sentences": {
            "zimmer_reservieren.mp3": "Ich möchte ein Zimmer reservieren.",
            "einzelzimmer_doppelzimmer.mp3": "Ein Einzelzimmer oder Doppelzimmer?",
            "schluessel_bitte.mp3": "Den Schlüssel, bitte.",
            "fruehstueck_inklusive.mp3": "Ist das Frühstück inklusive?",
            "wlan_password.mp3": "Wie ist das WLAN-Passwort?",
            "rechnung_bezahlen.mp3": "Ich möchte die Rechnung bezahlen.",
            "auschecken_wann.mp3": "Wann muss ich auschecken?",
            "koffer_zimmer.mp3": "Können Sie meinen Koffer aufs Zimmer bringen?",
            "tourist_information.mp3": "Wo ist die Touristeninformation?",
            "stadtplan_haben.mp3": "Haben Sie einen Stadtplan?"
        },
        "dialogues": {
            "d12_01.mp3": "Guten Abend! Haben Sie ein Zimmer frei?",
            "d12_02.mp3": "Ja, für wie viele Nächte?",
            "d12_03.mp3": "Für drei Nächte.",
            "d12_04.mp3": "Ein Einzelzimmer kostet 89 Euro pro Nacht.",
            "d12_05.mp3": "Das ist in Ordnung.",
            "d12_06.mp3": "Hier ist Ihr Schlüssel, Zimmer 205.",
            "d12_07.mp3": "Wo ist der Aufzug?",
            "d12_08.mp3": "Geradeaus und dann rechts.",
            "d12_09.mp3": "Gibt es hier einen Safe?",
            "d12_10.mp3": "Ja, in Ihrem Zimmer.",
            "d12_11.mp3": "Wann gibt es Frühstück?",
            "d12_12.mp3": "Von 7 bis 10 Uhr im Erdgeschoss.",
            "d12_13.mp3": "Können Sie mir ein Taxi rufen?",
            "d12_14.mp3": "Gern, wohin möchten Sie?",
            "d12_15.mp3": "Zum Bahnhof, bitte."
        }
    }
    
    # Chapter 13 - Kultur und Ausgehen (Culture and Going Out)
    ch13_data = {
        "sentences": {
            "konzert_besuchen.mp3": "Wir besuchen ein Konzert.",
            "theater_karten.mp3": "Haben Sie noch Karten für das Theater?",
            "museum_oeffnungszeiten.mp3": "Wie sind die Öffnungszeiten vom Museum?",
            "ausstellung_interessant.mp3": "Die Ausstellung ist sehr interessant.",
            "kino_film.mp3": "Welcher Film läuft im Kino?",
            "restaurant_reservierung.mp3": "Ich hätte gern eine Reservierung.",
            "kellner_rechnung.mp3": "Herr Kellner, die Rechnung bitte!",
            "cafe_kuchen.mp3": "Im Café gibt es leckeren Kuchen.",
            "bar_cocktail.mp3": "In der Bar trinken wir einen Cocktail.",
            "disco_tanzen.mp3": "In der Disco können wir tanzen."
        },
        "dialogues": {
            "d13_01.mp3": "Was machen wir heute Abend?",
            "d13_02.mp3": "Wir könnten ins Kino gehen.",
            "d13_03.mp3": "Gute Idee! Was läuft denn?",
            "d13_04.mp3": "Ein neuer Actionfilm.",
            "d13_05.mp3": "Um wie viel Uhr beginnt er?",
            "d13_06.mp3": "Um 20:15 Uhr.",
            "d13_07.mp3": "Haben Sie einen Tisch für zwei Personen?",
            "d13_08.mp3": "Ja, am Fenster oder lieber in der Mitte?",
            "d13_09.mp3": "Am Fenster, bitte.",
            "d13_10.mp3": "Die Speisekarte, bitte.",
            "d13_11.mp3": "Was können Sie empfehlen?",
            "d13_12.mp3": "Unser Schnitzel ist sehr beliebt.",
            "d13_13.mp3": "Dann nehme ich das Schnitzel.",
            "d13_14.mp3": "Und was möchten Sie trinken?",
            "d13_15.mp3": "Ein Bier, bitte."
        }
    }
    
    # Chapter 14 - Prüfungsvorbereitung (Exam Preparation)
    ch14_data = {
        "sentences": {
            "deutsch_lernen.mp3": "Ich lerne seit einem Jahr Deutsch.",
            "pruefung_schwer.mp3": "Die Prüfung war sehr schwer.",
            "grammatik_ueben.mp3": "Ich muss mehr Grammatik üben.",
            "vokabeln_wiederholen.mp3": "Wir wiederholen die Vokabeln.",
            "sprechen_verbessern.mp3": "Mein Sprechen muss sich verbessern.",
            "hoeren_verstehen.mp3": "Das Hören und Verstehen ist wichtig.",
            "schreiben_ueben.mp3": "Ich übe das Schreiben jeden Tag.",
            "lesen_macht_spass.mp3": "Lesen macht mir großen Spaß.",
            "kurs_beendet.mp3": "Der Kurs ist fast beendet.",
            "zertifikat_bekommen.mp3": "Ich bekomme hoffentlich das Zertifikat."
        },
        "dialogues": {
            "d14_01.mp3": "Bist du nervös wegen der Prüfung?",
            "d14_02.mp3": "Ja, sehr! Und du?",
            "d14_03.mp3": "Auch ein bisschen.",
            "d14_04.mp3": "Hast du gut gelernt?",
            "d14_05.mp3": "Ich hoffe es! Jeden Tag zwei Stunden.",
            "d14_06.mp3": "Was war am schwierigsten für dich?",
            "d14_07.mp3": "Die Grammatik, besonders die Artikel.",
            "d14_08.mp3": "Das verstehe ich gut.",
            "d14_09.mp3": "Wie lange lernst du schon Deutsch?",
            "d14_10.mp3": "Seit acht Monaten.",
            "d14_11.mp3": "Warum lernst du Deutsch?",
            "d14_12.mp3": "Ich möchte in Deutschland studieren.",
            "d14_13.mp3": "Das ist ein guter Grund!",
            "d14_14.mp3": "Viel Erfolg bei der Prüfung!",
            "d14_15.mp3": "Danke! Dir auch!"
        }
    }
    
    all_chapters = {
        12: ch12_data,
        13: ch13_data,
        14: ch14_data
    }
    
    print("🔊 Creating missing German audio files for Chapters 12-14...")
    
    for chapter_num, chapter_data in all_chapters.items():
        print(f"\n" + "="*50)
        print(f"📚 CHAPTER {chapter_num}")
        print("="*50)
        
        # Create sentences
        sentences = chapter_data["sentences"]
        print(f"\n📝 Creating {len(sentences)} Chapter {chapter_num} sentence audio files...")
        for filename, text in sentences.items():
            filepath = f"audio/sentences/{filename}"
            if not os.path.exists(filepath):
                try:
                    communicate = edge_tts.Communicate(text, voice, rate=rate)
                    await communicate.save(filepath)
                    print(f"✅ Created: {filename} -> {text}")
                except Exception as e:
                    print(f"❌ Error creating {filename}: {e}")
            else:
                print(f"⏭️  Skipped: {filename} (already exists)")
        
        # Create dialogues
        dialogues = chapter_data["dialogues"]
        print(f"\n💬 Creating {len(dialogues)} Chapter {chapter_num} dialogue audio files...")
        for filename, text in dialogues.items():
            filepath = f"audio/dialogues/{filename}"
            if not os.path.exists(filepath):
                try:
                    communicate = edge_tts.Communicate(text, voice, rate=rate)
                    await communicate.save(filepath)
                    print(f"✅ Created: {filename} -> {text}")
                except Exception as e:
                    print(f"❌ Error creating {filename}: {e}")
            else:
                print(f"⏭️  Skipped: {filename} (already exists)")
        
        print(f"\n✅ Chapter {chapter_num} complete!")
    
    print("\n" + "="*60)
    print("🎉 ALL CHAPTERS 12-14 AUDIO CREATION COMPLETE!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(create_chapters_12_14_audio())