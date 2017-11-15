from django.db import models

INSTRUMENT_SHORT_NAME_LEN = 4
INSTRUMENT_FULL_NAME_LEN = 20


class Instrument(models.Model):
    short_name = models.CharField(max_length=INSTRUMENT_SHORT_NAME_LEN)
    full_name = models.CharField(max_length=INSTRUMENT_FULL_NAME_LEN)