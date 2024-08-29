import pyaudio
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


p = pyaudio.PyAudio()
recognizer = sr.Recognizer()

def transcribe_audio_offline():
    recognizer = sr.Recognizer()
    with sr.AudioFile("test_audio.wav") as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_sphinx(audio_data)
            print(f"Transcrição (offline): {text}")
        except sr.UnknownValueError:
            print("Áudio não compreendido (offline)")
        except sr.RequestError as e:
            print(f"Erro na requisição: {e}")

transcribe_audio_offline()