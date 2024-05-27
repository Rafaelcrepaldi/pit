import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-2].id)

engine.say("eu vou falar este texto")
engine.runAndWait()