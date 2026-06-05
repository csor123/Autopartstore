from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")