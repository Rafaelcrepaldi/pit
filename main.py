import customtkinter as ctk
from httpcore import stream
from numpy import rec
from core import SystemInfo, TaskManager, NumberMapper
from voice import TextToSpeech
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import threading
from google_search import GoogleSearch  # Certifique-se de importar a classe correta

# Inicialização dos gerenciadores
task_manager = TaskManager()
number_mapper = NumberMapper()
tts = TextToSpeech()

# Inicialização do modelo e reconhecedor Vosk
model = Model("model")  # Substitua "model" pelo caminho do seu modelo Vosk
rec = KaldiRecognizer(model, 16000)
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Inicializa a classe GoogleSearch com sua chave de API e ID do mecanismo de pesquisa
google_search = GoogleSearch(api_key='AIzaSyAwlBQKFcBgIar7F0-s8Yq-2CEmmjoSTmU', search_engine_id='124481474049d49d9')

# Função para reconhecimento de comandos por voz
def get_voice_input(prompt):
    tts.speak(prompt)
    while True:
        data = stream.read(2048)
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            if result is not None:
                text = result['text']
                return text

def reconhecer_comandos_por_voz(audio):
    def reconhecimento_thread():
        while True:
            data = stream.read(2048)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result = json.loads(result)

                if result is not None:  # Verifica se result não é None e se 'text' está presente
                    text = result['text']
                    print("Comando reconhecido:", text)

                    if text == 'horas' or text == 'hora':
                        obter_horas()
                    elif text == 'data' or text == 'dia':
                        obter_data()
                    elif text == 'google' or text == 'abrir google':
                        tts.speak("abrindo google...")
                        abrir_google()
                    else:
                        resposta = google_search.responder_pergunta(text)  # Uso correto da instância google_search
                        tts.speak(resposta)
                        resultado.set(resposta)

        # Certifique-se de fechar o fluxo manualmente após a conclusão
        stream.stop_stream()
        stream.close()
        audio.terminate()

    # Inicia o thread para execução do reconhecimento de comandos por voz
    threading.Thread(target=reconhecimento_thread).start()

# Funções de Interface
def obter_horas():
    resposta = SystemInfo.get_time()
    tts.speak(resposta)

def obter_data():
    resposta = SystemInfo.get_date()
    tts.speak(resposta)

def abrir_google():
    resposta = SystemInfo.open_google()
    tts.speak(resposta)

# Adicionar histórico de comandos
historico_comandos = []


# Configuração da Interface Gráfica
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

app = ctk.CTk()
app.geometry("600x400")
app.title("Assistente Virtual")

frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

titulo = ctk.CTkLabel(frame, text="Assistente Virtual", font=("Arial", 24))
titulo.pack(pady=12, padx=10)

resultado = ctk.StringVar()

# Widgets da Interface
btn_horas = ctk.CTkButton(frame, text="Obter Horas", command=obter_horas)
btn_horas.pack(pady=10)

btn_data = ctk.CTkButton(frame, text="Obter Data", command=obter_data)
btn_data.pack(pady=10)

btn_google = ctk.CTkButton(frame, text="Abrir Google", command=abrir_google)
btn_google.pack(pady=10)

# Inicializa o PyAudio fora da função de reconhecimento
audio = pyaudio.PyAudio()

# Chama a função de reconhecimento passando a instância do PyAudio como argumento
btn_reconhecer_voz = ctk.CTkButton(frame, text="Reconhecer Comandos por Voz", command=lambda: reconhecer_comandos_por_voz(audio))
btn_reconhecer_voz.pack(pady=10)

# Botão para perguntas gerais
btn_perguntas_gerais = ctk.CTkButton(frame, text="Perguntar", command=lambda: google_search.responder_pergunta("Qual é a capital da França?"))
btn_perguntas_gerais.pack(pady=10)

# Label para mostrar o resultado
label_resultado = ctk.CTkLabel(frame, textvariable=resultado, font=("Arial", 18))
label_resultado.pack(pady=20)

# Label para mostrar o histórico de comandos
label_historico = ctk.CTkLabel(frame, text="", font=("Arial", 12), justify="left")
label_historico.pack(pady=10)

app.mainloop()
