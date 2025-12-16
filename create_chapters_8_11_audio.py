#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create missing German sentences and dialogues audio files for chapters 8-14
"""
import asyncio
import edge_tts
import os

async def create_chapters_8_14_audio():
    """Create missing audio files for chapters 8-14"""
    
    # German voice settings
    voice = "de-DE-KatjaNeural"
    rate = "-20%"  # Slower for learning
    
    # Chapter 8 - Körper und Gesundheit (Body and Health)
    ch8_data = {
        "sentences": {
            "kopfschmerzen.mp3": "Ich habe Kopfschmerzen.",
            "bauch_weh.mp3": "Mir tut der Bauch weh.",
            "bin_krank.mp3": "Ich bin krank.",
            "zum_arzt.mp3": "Ich muss zum Arzt gehen.",
            "hat_fieber.mp3": "Sie hat Fieber.",
            "medikamente_nehmen.mp3": "Du musst Medikamente nehmen.",
            "erkaeltung.mp3": "Ich habe eine Erkältung.",
            "ausruhen.mp3": "Sie müssen sich ausruhen.",
            "gute_besserung.mp3": "Gute Besserung!",
            "apotheke_wo.mp3": "Wo ist die Apotheke?"
        },
        "dialogues": {
            "d8_01.mp3": "Guten Tag! Was fehlt Ihnen?",
            "d8_02.mp3": "Ich habe Kopfschmerzen und Fieber.",
            "d8_03.mp3": "Seit wann haben Sie diese Symptome?",
            "d8_04.mp3": "Seit gestern Abend.",
            "d8_05.mp3": "Ich untersuche Sie jetzt.",
            "d8_06.mp3": "Sie haben eine Grippe.",
            "d8_07.mp3": "Nehmen Sie diese Tabletten dreimal täglich.",
            "d8_08.mp3": "Mir tut alles weh!",
            "d8_09.mp3": "Was ist denn los?",
            "d8_10.mp3": "Ich bin beim Sport gefallen.",
            "d8_11.mp3": "Tut das hier weh?",
            "d8_12.mp3": "Entschuldigung, wo ist die Apotheke?",
            "d8_13.mp3": "Gleich um die Ecke, neben der Bank.",
            "d8_14.mp3": "Haben Sie etwas gegen Husten?",
            "d8_15.mp3": "Ja, hier ist ein guter Hustensaft."
        }
    }
    
    # Chapter 9 - Zeit und Datum (Time and Date)
    ch9_data = {
        "sentences": {
            "wie_spaet.mp3": "Wie spät ist es?",
            "acht_uhr.mp3": "Es ist acht Uhr.",
            "viertel_nach.mp3": "Es ist Viertel nach drei.",
            "halb_fuenf.mp3": "Es ist halb fünf.",
            "welcher_tag.mp3": "Welcher Tag ist heute?",
            "montag_heute.mp3": "Heute ist Montag.",
            "wann_termin.mp3": "Wann haben Sie Zeit?",
            "um_zwei.mp3": "Um zwei Uhr nachmittags.",
            "frueh_aufstehen.mp3": "Ich muss früh aufstehen.",
            "spaet_kommen.mp3": "Entschuldigung, ich komme zu spät."
        },
        "dialogues": {
            "d9_01.mp3": "Wie spät ist es denn?",
            "d9_02.mp3": "Es ist schon zehn nach acht.",
            "d9_03.mp3": "Oh nein! Ich komme zu spät zur Arbeit!",
            "d9_04.mp3": "Wann treffen wir uns?",
            "d9_05.mp3": "Um halb drei am Hauptbahnhof.",
            "d9_06.mp3": "Welcher Tag ist heute?",
            "d9_07.mp3": "Heute ist Mittwoch, der 15. Mai.",
            "d9_08.mp3": "Haben Sie morgen Zeit?",
            "d9_09.mp3": "Ja, um wie viel Uhr?",
            "d9_10.mp3": "Um Viertel vor zwei.",
            "d9_11.mp3": "Wann fahren Sie in den Urlaub?",
            "d9_12.mp3": "Am nächsten Freitag.",
            "d9_13.mp3": "Wie lange arbeiten Sie?",
            "d9_14.mp3": "Von acht bis siebzehn Uhr.",
            "d9_15.mp3": "Das ist aber lang!"
        }
    }
    
    # Chapter 10 - Verkehr und Transport (Traffic and Transport)
    ch10_data = {
        "sentences": {
            "mit_bus.mp3": "Ich fahre mit dem Bus zur Arbeit.",
            "auto_parken.mp3": "Wo kann ich mein Auto parken?",
            "bahnhof_wo.mp3": "Entschuldigung, wo ist der Bahnhof?",
            "zug_verspaetet.mp3": "Der Zug hat Verspätung.",
            "ticket_kaufen.mp3": "Ich möchte ein Ticket kaufen.",
            "naechste_station.mp3": "Welche ist die nächste Station?",
            "umsteigen_muessen.mp3": "Sie müssen in München umsteigen.",
            "taxi_nehmen.mp3": "Wir nehmen ein Taxi.",
            "fahrrad_fahren.mp3": "Im Sommer fahre ich oft Fahrrad.",
            "stau_autobahn.mp3": "Auf der Autobahn ist Stau."
        },
        "dialogues": {
            "d10_01.mp3": "Entschuldigung, wie komme ich zum Bahnhof?",
            "d10_02.mp3": "Nehmen Sie die U-Bahn Linie 3.",
            "d10_03.mp3": "Wo muss ich aussteigen?",
            "d10_04.mp3": "An der Haltestelle Hauptbahnhof.",
            "d10_05.mp3": "Wann fährt der nächste Zug nach Berlin?",
            "d10_06.mp3": "Um 14:30 von Gleis 7.",
            "d10_07.mp3": "Taxi! Sind Sie frei?",
            "d10_08.mp3": "Ja, wohin möchten Sie?",
            "d10_09.mp3": "Zum Flughafen, bitte.",
            "d10_10.mp3": "Das dauert etwa 30 Minuten.",
            "d10_11.mp3": "Ist hier ein Parkplatz?",
            "d10_12.mp3": "Ja, aber er kostet 2 Euro pro Stunde.",
            "d10_13.mp3": "Der Bus kommt gleich.",
            "d10_14.mp3": "Haben Sie einen Fahrplan?",
            "d10_15.mp3": "Ja, hier bitte."
        }
    }
    
    # Chapter 11 - Wetter und Jahreszeiten (Weather and Seasons)
    ch11_data = {
        "sentences": {
            "wie_wetter.mp3": "Wie ist das Wetter heute?",
            "regnet_heute.mp3": "Heute regnet es.",
            "sonne_scheint.mp3": "Die Sonne scheint.",
            "sehr_kalt.mp3": "Es ist sehr kalt.",
            "fruehling_schoen.mp3": "Der Frühling ist schön.",
            "sommer_heiss.mp3": "Im Sommer ist es heiß.",
            "herbst_windig.mp3": "Im Herbst ist es windig.",
            "winter_schnee.mp3": "Im Winter schneit es.",
            "regenschirm_brauchen.mp3": "Ich brauche einen Regenschirm.",
            "jacke_anziehen.mp3": "Du solltest eine Jacke anziehen."
        },
        "dialogues": {
            "d11_01.mp3": "Wie wird das Wetter morgen?",
            "d11_02.mp3": "Es soll regnen.",
            "d11_03.mp3": "Dann brauche ich einen Regenschirm.",
            "d11_04.mp3": "Es ist so heiß heute!",
            "d11_05.mp3": "Ja, 35 Grad im Schatten.",
            "d11_06.mp3": "Was ist deine Lieblingsjahreszeit?",
            "d11_07.mp3": "Ich mag den Herbst am liebsten.",
            "d11_08.mp3": "Warum denn?",
            "d11_09.mp3": "Die Blätter sind so schön bunt.",
            "d11_10.mp3": "Schneit es schon?",
            "d11_11.mp3": "Nein, aber es ist sehr kalt.",
            "d11_12.mp3": "Im Frühling blühen die Blumen.",
            "d11_13.mp3": "Ja, und die Vögel singen wieder.",
            "d11_14.mp3": "Das Wetter ist heute perfekt.",
            "d11_15.mp3": "Stimmt, lass uns spazieren gehen!"
        }
    }
    
    all_chapters = {
        8: ch8_data,
        9: ch9_data,
        10: ch10_data,
        11: ch11_data
    }
    
    print("🔊 Creating missing German audio files for Chapters 8-11...")
    
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
    print("🎉 ALL CHAPTERS 8-11 AUDIO CREATION COMPLETE!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(create_chapters_8_14_audio())