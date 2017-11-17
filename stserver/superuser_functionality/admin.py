from django.contrib import admin

from .models import Currency
from .models import Instrument

admin.site.register(Currency)
admin.site.register(Instrument)
