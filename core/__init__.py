import datetime
import os
import webbrowser
import pyaudio  
import requests


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
