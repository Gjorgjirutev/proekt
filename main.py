from openai import OpenAI
client = OpenAI()

audio_file = open("\Users\PCI\Music\Pythonaudio", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")