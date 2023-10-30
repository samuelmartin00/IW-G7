from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse('HOLA MUNDO')

def despedida(request):
    return HttpResponse('ADIOS')

def grupo(request):
    return HttpResponse('GRUPO INFO')

def sala(request):
    return HttpResponse('SALA INFO')