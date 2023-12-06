from openai import OpenAI
from docx import Document
client = OpenAI()
audio_file_path = open("audio.mp3", "rb") w
text = audio_file_path
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create("whisper-1", audio_file)
    return transcription[text]

print(text)