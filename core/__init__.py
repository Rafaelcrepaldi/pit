import datetime
import os
import webbrowser
import pyaudio  
import requests
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer
    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é {} de {} de {}.'.format(now.day, now.month, now.year)
        return answer
    @staticmethod
    def open_google():
        webbrowser.open('www.google.com.br')
        answer = 'abrindo o google'
        return answer
    
    @staticmethod
    def open_youtube():
        webbrowser.open('www.youtube.com')
    
    @staticmethod
    def open_whatsapp():
        webbrowser.open('https://web.whatsapp.com/')

    @staticmethod
    def open_facebook():
        webbrowser.open('https://www.facebook.com/')

    @staticmethod
    def open_instagram():
        webbrowser.open('https://www.instagram.com/')


class TaskManager:
    tasks = []

    @staticmethod
    def add_task(task):
        TaskManager.tasks.append(task)

    @staticmethod
    def remove_task(task_index):
        if 0 <= task_index < len(TaskManager.tasks):
            del TaskManager.tasks[task_index]

    @staticmethod
    def get_tasks():
        return TaskManager.tasks

class CalendarManager:
    def __init__(self):
        self.creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/calendar'])
        self.service = build('calendar', 'v3', credentials=self.creds)

    def create_event(self, summary, start_datetime, end_datetime):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'America/Los_Angeles',
            },
        }
        self.service.events().insert(calendarId='primary', body=event).execute()

class NumberMapper:
    def __init__(self):
        self.number_map = self._create_number_map()

    def _create_number_map(self):
        units = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        teens = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
        tens = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        hundreds = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
        number_map = {}

        for i in range(1, 10):
            number_map[units[i]] = i

        for i in range(10, 20):
            number_map[teens[i - 10]] = i

        for i in range(2, 10):
            for j in range(0, 10):
                if j == 0:
                    number_map[tens[i]] = i * 10
                else:
                    number_map[f"{tens[i]} e {units[j]}"] = i * 10 + j

        for i in range(1, 10):
            for j in range(0, 100):
                if j == 0:
                    number_map[hundreds[i]] = i * 100
                else:
                    if j < 10:
                        number_map[f"{hundreds[i]} e {units[j]}"] = i * 100 + j
                    elif j < 20:
                        number_map[f"{hundreds[i]} e {teens[j - 10]}"] = i * 100 + j
                    else:
                        tens_part = j // 10
                        units_part = j % 10
                        if units_part == 0:
                            number_map[f"{hundreds[i]} e {tens[tens_part]}"] = i * 100 + j
                        else:
                            number_map[f"{hundreds[i]} e {tens[tens_part]} e {units[units_part]}"] = i * 100 + j

        for i in range(1, 10):
            for j in range(0, 1000):
                if j == 0:
                    number_map[f"{units[i]} mil"] = i * 1000
                else:
                    if j < 10:
                        number_map[f"{units[i]} mil e {units[j]}"] = i * 1000 + j
                    elif j < 20:
                        number_map[f"{units[i]} mil e {teens[j - 10]}"] = i * 1000 + j
                    elif j < 100:
                        tens_part = j // 10
                        units_part = j % 10
                        if units_part == 0:
                            number_map[f"{units[i]} mil e {tens[tens_part]}"] = i * 1000 + j
                        else:
                            number_map[f"{units[i]} mil e {tens[tens_part]} e {units[units_part]}"] = i * 1000 + j
                    else:
                        hundreds_part = j // 100
                        remainder = j % 100
                        if remainder == 0:
                            number_map[f"{units[i]} mil e {hundreds[hundreds_part]}"] = i * 1000 + j
                        else:
                            if remainder < 10:
                                number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {units[remainder]}"] = i * 1000 + j
                            elif remainder < 20:
                                number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {teens[remainder - 10]}"] = i * 1000 + j
                            else:
                                tens_part = remainder // 10
                                units_part = remainder % 10
                                if units_part == 0:
                                    number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {tens[tens_part]}"] = i * 1000 + j
                                else:
                                    number_map[f"{units[i]} mil e {hundreds[hundreds_part]} e {tens[tens_part]} e {units[units_part]}"] = i * 1000 + j

        return number_map

    def map_number(self, text):
        return self.number_map.get(text, text)  # Retorna o texto original se não encontrar no mapa
