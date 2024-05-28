import requests

class CurrencyConverter:
    API_KEY = 'sua_api_key'  # Substitua pela sua chave de API da ExchangeRate-API

    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        url = f'https://v6.exchangerate-api.com/v6/{CurrencyConverter.API_KEY}/pair/{from_currency}/{to_currency}/{amount}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            conversion_result = data['conversion_result']
            return f'{amount} {from_currency} é igual a {conversion_result} {to_currency}.'
        else:
            return 'Não foi possível converter a moeda no momento.'
