from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def grupo(request):
    return HttpResponse("")

def sala(request):
    return HttpResponse("")

def musico(request):
    return HttpResponse("")