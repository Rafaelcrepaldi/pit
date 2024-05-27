from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            if text == 'assistente que horas são' or text == 'assistente me diga as horas' or text == 'assistente horas':
                speak(core.SystemInfo.get_time())
            elif text == 'assistente que dia é hoje' or text == 'assistente me diga o dia':
                speak(core.SystemInfo.get_date())
            elif text == 'assistente abra o google' or text == 'assistente google':
                speak('abrindo o google')
                core.SystemInfo.open_google()
            elif text == 'assistente abra o youtube':
                core.SystemInfo.open_youtube()
                speak('abrindo o youtube')
            elif text == 'assistente abra o ataque' or text == 'assistente abra ato' or text == 'assistente ataque':
                core.SystemInfo.open_whatsapp()
                speak('abrindo o whatsapp')
            elif text == 'assistente abra o facebook':
                core.SystemInfo.open_facebook()
                speak('abrindo o facebook')
            elif text == 'assistente abra o instagram':
                core.SystemInfo.open_instagram()
                speak('abrindo o instagram')
            elif text == 'assistente adicione uma tarefa' or text == 'assistente crie uma tarefa':
                speak('Qual é a sua nova tarefa?')
                new_task_result = input()  # Obtém o resultado final da transcrição
                core.TaskManager.add_task(new_task_result)
                speak('Tarefa adicionada com sucesso.')
            elif text == 'assistente liste minhas tarefas' or text == 'assistente mostre minhas tarefas':
                tasks = core.TaskManager.get_tasks()
                if len(tasks) > 0:
                    speak('Aqui estão suas tarefas:')
                    for index, task in enumerate(tasks):
                        speak(f'Tarefa {index + 1}: {task}')
                else:
                    speak('Você não tem tarefas pendentes.')

                        