from django.urls import path
from . import views

urlpatterns = [
    #URLS
    path('', views.inicio, name='main'),
    path('gbwye', views.despedida, name='gbwye'),
    
    path('listgrupo', views.listaGrupo, name='lgrp'),
    path('listsala', views.listaSala, name='lsal'),
    path('listmusico', views.listaMusico, name='lmuso'),
    
]
