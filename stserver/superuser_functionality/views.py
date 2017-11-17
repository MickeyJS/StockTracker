from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("Superuser login")


def show_all_instruments(request):
    return HttpResponse("All available instruments will be listed here")


def add_new_instrument(request):
    return HttpResponse("Add new instrument that will be displayed and available to watch by users")


def superuser_panel(request):
    return HttpResponse("Superuser panel with listed options")