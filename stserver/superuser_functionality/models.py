from django.db import models

INSTRUMENT_SHORT_NAME_LEN = 4
INSTRUMENT_FULL_NAME_LEN = 20
INSTRUMENT_CURRENCY_LEN = 7


class Instrument(models.Model):
    short_name = models.CharField(max_length=INSTRUMENT_SHORT_NAME_LEN)
    full_name = models.CharField(max_length=INSTRUMENT_FULL_NAME_LEN)
    price = models.FloatField(default=0.0)
    currency = models.CharField(max_length=INSTRUMENT_CURRENCY_LEN, default="USD")

    def __str__(self):
        return "{} {} {} {}".format(self.short_name, self.full_name, str(self.price), self.currency)