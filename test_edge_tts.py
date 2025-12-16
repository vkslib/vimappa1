import asyncio
import edge_tts

async def test_edge_tts():
    text = "Hallo, dies ist ein Test."
    output_path = "test_audio.mp3"
    voice = "de-DE-KatjaNeural"
    rate = "-20%"

    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_path)
    print(f"Generated test audio: {output_path}")

if __name__ == "__main__":
    asyncio.run(test_edge_tts())