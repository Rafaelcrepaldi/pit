import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[-2].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
