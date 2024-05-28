import requests

class GoogleSearch:
    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    def search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.search_engine_id}&lr=lang_pt"
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
            # Processa o primeiro resultado relevante
            resposta = results[0].get('snippet', 'Desculpe, não consegui encontrar uma resposta para a sua pergunta.')
            return resposta
        else:
            return "Desculpe, não consegui encontrar uma resposta para a sua pergunta."
