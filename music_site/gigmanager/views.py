from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("HolaMundo")

def grupo(request):
    return HttpResponse("")

def sala(request):
    return HttpResponse("")

def musico(request):
    return HttpResponse("")