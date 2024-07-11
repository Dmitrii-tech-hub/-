# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:36:00 2024

@author: dmitr
"""

# Все классы спрятать в файле

import requests
import json

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str, keys: dict):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://api.exchangerate-api.com/v4/latest/{base_ticker}')
        rates = json.loads(r.content)['rates']
        
        if quote_ticker not in rates:
            raise APIException(f'Не удалось получить курс для валюты {quote}.')

        total_quote = rates[quote_ticker] * amount

        return total_quote

    

    
    
