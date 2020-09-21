from django.http import  HttpResponse

def index(request):
    return HttpResponse('<h1>www.priceaction.ai - homepage</h1><hr>');