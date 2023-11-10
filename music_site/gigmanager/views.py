from django.shortcuts import render
from django.http import HttpResponse 

from .models import Grupo, Sitio, Musico

# Create your views here.
def inicio(request):
    return HttpResponse('HOLA MUNDO')

def despedida(request):
    return HttpResponse('ADIOS')

def listaGrupo(request):
    grupos = Grupo.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([g.nombre for g in grupos])

    return HttpResponse(cadenaDeTexto)

def listaSala(request):
    salas = Sitio.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([s.nombre for s in salas])

    return HttpResponse(cadenaDeTexto)
    
def listaMusico(request):
    musicos = Musico.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([m.nombre for m in musicos])

    return HttpResponse(cadenaDeTexto)