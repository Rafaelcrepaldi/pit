from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core
from core import NumberMapper  # Importe a nova classe

# Inicialização da fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

# Função para falar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Inicialização do reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Inicialização dos gerenciadores de tarefas e calendário
task_manager = core.TaskManager()
calendar_manager = core.CalendarManager()
number_mapper = NumberMapper()  # Inicialize o mapeador de números

# Função para obter entrada de voz e convertê-la em texto
def get_voice_input(prompt):
    speak(prompt)
    while True:
        data = stream.read(2048)
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            if result is not None:
                text = result['text']
                return text

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
                speak('Escolha uma das seguintes opções de tarefa: 1. Comprar leite 2. Ligar para cliente 3. Enviar email')
                task_choice = get_voice_input('Por favor, diga o número da opção:')
                task_choice = number_mapper.map_number(task_choice)
                if task_choice == 1:
                    task_manager.add_task('Comprar leite')
                elif task_choice == 2:
                    task_manager.add_task('Ligar para cliente')
                elif task_choice == 3:
                    task_manager.add_task('Enviar email')
                speak('Tarefa adicionada com sucesso.')
            elif text == 'assistente liste minhas tarefas' or text == 'assistente mostre minhas tarefas':
                tasks = task_manager.get_tasks()
                if len(tasks) > 0:
                    speak('Aqui estão suas tarefas:')
                    for index, task in enumerate(tasks):
                        speak(f'Tarefa {index + 1}: {task}')
                else:
                    speak('Você não tem tarefas pendentes.')
            elif text == 'assistente crie um evento no calendário':
                summary = get_voice_input('Qual é o resumo do evento?')
                start_date = get_voice_input('Qual é a data de início do evento? (Formato: YYYY-MM-DD)')
                start_time = get_voice_input('Qual é a hora de início do evento? (Formato: HH:MM)')
                end_date = get_voice_input('Qual é a data de término do evento? (Formato: YYYY-MM-DD)')
                end_time = get_voice_input('Qual é a hora de término do evento? (Formato: HH:MM)')

                start_datetime = f'{start_date}T{start_time}:00'
                end_datetime = f'{end_date}T{end_time}:00'
                calendar_manager.create_event(summary, start_datetime, end_datetime)
                speak('Evento criado com sucesso no seu calendário.')
