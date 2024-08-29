import pyaudio
import wave

# Configurações de áudio
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

def capture_and_save_audio():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Gravando... Pressione Ctrl+C para parar.")

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
    except KeyboardInterrupt:
        print("Gravação finalizada.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Salvar o áudio capturado em um arquivo WAV
    wf = wave.open("test_audio.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

capture_and_save_audio()
