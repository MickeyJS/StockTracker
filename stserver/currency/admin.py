from django.contrib import admin
from .models import Currency
from .models import Rate

admin.site.register(Currency)
admin.site.register(Rate)
