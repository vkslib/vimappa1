#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create correct German audio files for Chapters 12-13
"""
import asyncio
import edge_tts
import os

async def create_correct_chapters_12_13_audio():
    """Create correct audio files for Chapters 12-13"""
    
    voice = "de-DE-KatjaNeural"
    rate = "-20%"
    
    # Chapter 12 - Medien und Kommunikation (Media and Communication)
    ch12_sentences = {
        "unit12_sent01.mp3": "Ich schicke dir eine E-Mail.",
        "unit12_sent02.mp3": "Ruf mich später an!",
        "unit12_sent03.mp3": "Ich surfe gern im Internet.",
        "unit12_sent04.mp3": "Ich lerne Deutsch, weil ich in Berlin arbeite.",
        "unit12_sent05.mp3": "Ich denke, dass das Handy wichtig ist.",
        "unit12_sent06.mp3": "Wenn ich Zeit habe, sehe ich einen Film.",
        "unit12_sent07.mp3": "Ich lese gern die Zeitung.",
        "unit12_sent08.mp3": "Das Internet ist sehr praktisch.",
        "unit12_sent09.mp3": "Ich chatte mit meinen Freunden.",
        "unit12_sent10.mp3": "Kannst du mir deine Nummer geben?"
    }
    
    ch12_dialogues = {
        "unit12_dialog01.mp3": "Hallo, hier ist Anna.",
        "unit12_dialog02.mp3": "Hi Anna! Wie geht's dir?",
        "unit12_dialog03.mp3": "Gut, danke! Was machst du?",
        "unit12_dialog04.mp3": "Ich schaue Fernsehen.",
        "unit12_dialog05.mp3": "Was läuft denn?",
        "unit12_dialog06.mp3": "Ein interessanter Dokumentarfilm.",
        "unit12_dialog07.mp3": "Hast du meine SMS bekommen?",
        "unit12_dialog08.mp3": "Ja, danke für die Information.",
        "unit12_dialog09.mp3": "Schickst du mir die Fotos per E-Mail?",
        "unit12_dialog10.mp3": "Natürlich, mache ich gleich.",
        "unit12_dialog11.mp3": "Mein Computer ist kaputt.",
        "unit12_dialog12.mp3": "Das ist ärgerlich.",
        "unit12_dialog13.mp3": "Kannst du mir helfen?",
        "unit12_dialog14.mp3": "Gern, komm vorbei.",
        "unit12_dialog15.mp3": "Vielen Dank!"
    }
    
    # Chapter 13 - Kultur und Feste (Culture and Festivals)  
    ch13_sentences = {
        "unit13_sent01.mp3": "Weihnachten ist ein wichtiges Fest.",
        "unit13_sent02.mp3": "Zu Ostern suchen Kinder Eier.",
        "unit13_sent03.mp3": "Der Karneval ist sehr bunt und lustig.",
        "unit13_sent04.mp3": "Ich gehe gern ins Theater.",
        "unit13_sent05.mp3": "Das Museum hat schöne Kunstwerke.",
        "unit13_sent06.mp3": "Die deutsche Kultur ist sehr interessant.",
        "unit13_sent07.mp3": "Welche Traditionen gibt es hier?",
        "unit13_sent08.mp3": "Im Dezember sind viele Märkte geöffnet.",
        "unit13_sent09.mp3": "Die Musik gefällt mir sehr gut.",
        "unit13_sent10.mp3": "Deutsche Feste sind sehr schön."
    }
    
    ch13_dialogues = {
        "unit13_dialog01.mp3": "Gehst du zum Oktoberfest?",
        "unit13_dialog02.mp3": "Ja, das ist eine tolle Tradition!",
        "unit13_dialog03.mp3": "Was trägst du denn?",
        "unit13_dialog04.mp3": "Ein traditionelles Dirndl.",
        "unit13_dialog05.mp3": "Wie feiert ihr Weihnachten?",
        "unit13_dialog06.mp3": "Wir schmücken den Weihnachtsbaum.",
        "unit13_dialog07.mp3": "Und dann gibt es Geschenke.",
        "unit13_dialog08.mp3": "Was ist dein Lieblingsfest?",
        "unit13_dialog09.mp3": "Ich mag den Karneval sehr.",
        "unit13_dialog10.mp3": "Die Kostüme sind so kreativ!",
        "unit13_dialog11.mp3": "Warst du schon mal in der Oper?",
        "unit13_dialog12.mp3": "Nein, aber ich möchte gern gehen.",
        "unit13_dialog13.mp3": "Die Musik ist wunderschön.",
        "unit13_dialog14.mp3": "Das kann ich mir vorstellen.",
        "unit13_dialog15.mp3": "Dann gehen wir zusammen hin!"
    }
    
    all_chapters = {
        12: {"sentences": ch12_sentences, "dialogues": ch12_dialogues},
        13: {"sentences": ch13_sentences, "dialogues": ch13_dialogues}
    }
    
    print("🔊 Creating correct German audio files for Chapters 12-13...")
    
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
                    await asyncio.sleep(0.3)
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
                    await asyncio.sleep(0.3)
                except Exception as e:
                    print(f"❌ Error creating {filename}: {e}")
            else:
                print(f"⏭️  Skipped: {filename} (already exists)")
        
        print(f"\n✅ Chapter {chapter_num} complete!")
    
    print("\n🎉 Chapters 12-13 audio creation complete!")

if __name__ == "__main__":
    asyncio.run(create_correct_chapters_12_13_audio())