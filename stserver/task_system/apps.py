from django.apps import AppConfig

import requests
import json

class TaskSystemConfig(AppConfig):
    name = 'task_system'

    """
    def ready(self):
        r = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey=1A777UAHWTQ1271V')
        if r.status_code == 200:
            data = json.loads(r.text)
            data = data['Realtime Currency Exchange Rate']
            short = data['1. From_Currency Code']
            full = data['2. From_Currency Name']

            #currency = Currency(short, full)
            #currency.save()
            print(short)
            print(full)
    """