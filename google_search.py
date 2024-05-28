import requests
import json

class GoogleSearch:
    def __init__(self, api_key, search_engine_id):
        self.api_key = 'AIzaSyAwlBQKFcBgIar7F0-s8Yq-2CEmmjoSTmU'
        self.search_engine_id = '124481474049d49d9'

    def search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.search_engine_id}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json()
            if 'items' in results:
                return results['items']
            else:
                return None
        else:
            return None

    def responder_pergunta(self, pergunta):
        results = self.search(pergunta)
        if results:
            resposta = results[0]['snippet']
            return resposta
        else:
            return "Desculpe, não consegui encontrar uma resposta para a sua pergunta."
