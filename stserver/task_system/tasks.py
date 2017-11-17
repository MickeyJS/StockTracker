from __future__ import absolute_import, unicode_literals
from celery import task

from django.db import models
from .models import Instrument

p = Dodavatel(nazov='Petr', dostupnost=1)
p.save()

@task()
def get_exchange_rate():
    r = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey=1A777UAHWTQ1271V')
    if r.status_code == 200:
        data = json.loads(r.text)
        data = data['Realtime Currency Exchange Rate']
        short = data['1. From_Currency Code']
        full = data['2. From_Currency Name']

        # currency = Currency(short, full)
        # currency.save()
        print(short)
        print(full)

"""
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "USD",
        "2. From_Currency Name": "United States Dollar",
        "3. To_Currency Code": "PLN",
        "4. To_Currency Name": "Polish Zloty",
        "5. Exchange Rate": "3.59356000",
        "6. Last Refreshed": "2017-11-17 13:02:20",
        "7. Time Zone": "UTC"
    }
}
"""

@task()
def get_sms():
    # Do something...