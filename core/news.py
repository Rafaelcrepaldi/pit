import requests

class News:
    API_KEY = 'sua_api_key'  # Substitua pela sua chave de API da NewsAPI

    @staticmethod
    def get_latest_headlines():
        url = f'https://newsapi.org/v2/top-headlines?country=br&apiKey={News.API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json()['articles']
            headlines = [article['title'] for article in articles[:5]]  # Pegue as 5 primeiras manchetes
            return headlines
        else:
            return 'Não foi possível obter as notícias no momento.'
