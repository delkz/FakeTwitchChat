import pyaudio
import vosk
import json

class AudioCapture:
    def __init__(self, model_path, device_index=None, chunk=1024, rate=16000, channels=1):
        self.chunk = chunk
        self.rate = rate
        self.channels = channels
        self.device_index = device_index
        # Verifique o caminho do modelo
        print(f"Loading model from: {model_path}")
        self.model = vosk.Model(model_path)
        self.recognizer = vosk.KaldiRecognizer(self.model, self.rate)
        self.p = pyaudio.PyAudio()
        self.stream = None

    def list_devices(self):
        print("Dispositivos de áudio disponíveis:")
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            print(f"Device {i}: {info['name']}")

    def start_stream(self):
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  input_device_index=self.device_index,
                                  frames_per_buffer=self.chunk)

    def stop_stream(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

    def transcribe(self):
        if self.stream:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                return result.get("text", "")
        return ""

    def close(self):
        self.stop_stream()
        self.p.terminate()
