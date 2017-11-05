from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Stock app index page</h1>")
