import pyaudio
import json
from vosk import Model, KaldiRecognizer

class VoiceRecognition:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()

    def get_voice_input(self):
        data = self.stream.read(2048)
        if self.recognizer.AcceptWaveform(data):
            result = self.recognizer.Result()
            result = json.loads(result)
            return result['text'] if result is not None else None
        return None

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
