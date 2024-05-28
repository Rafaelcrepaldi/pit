import datetime
import webbrowser

class SystemInfo:
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        return f'São {now.hour} horas e {now.minute} minutos.'

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        return f'Hoje é {now.day} de {now.month} de {now.year}.'

    @staticmethod
    def open_google():
        webbrowser.open('www.google.com.br')
        return f'abrindo o google'
    
    @staticmethod
    def open_youtube():
        webbrowser.open('www.youtube.com')
        return f'abrindo o youtube'
    
    @staticmethod
    def open_whatsapp():
        webbrowser.open('https://web.whatsapp.com/')
        return f'abrindo o whatsapp'


    @staticmethod
    def open_facebook():
        webbrowser.open('https://www.facebook.com/')
        return f'abrindo o facebook'

    @staticmethod
    def open_instagram():
        webbrowser.open('https://www.instagram.com/')
        return f'abrindo o instagram'
