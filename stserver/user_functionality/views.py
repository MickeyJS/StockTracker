from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

import requests
import json


def create_account(request):
    return HttpResponse("Site with account creation :)")


def login_user(request):
    return HttpResponse("Login logic will be here!")


def show_all_instruments(request):
    return HttpResponse("All available instruments will be listed here")


def show_user_instruments(request):
    return HttpResponse("User instruments will be listed here")


def change_user_data(request):
    return HttpResponse("Here user will be able to change telefon number, e-mail address...")