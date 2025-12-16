import asyncio
import edge_tts

async def test_connection():
    try:
        communicate = edge_tts.Communicate("Test", "en-US-AriaNeural")
        await communicate.save("test_connection.mp3")
        print("Connection to TTS service successful.")
    except Exception as e:
        print(f"Failed to connect to TTS service: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())