from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Currency

def index(request):
    all = Currency.objects.all()
    context = {'all_currencies' : all}
    return render(request, "index.html", context)

def detail(request, currency_id):
    try:
        currency = Currency.objects.get(pk=currency_id)
    except Currency.DoesNotExist:
        raise Http404("Waluta nie istnieje.")
    return render(request, "detail.html", {'currency' : currency})