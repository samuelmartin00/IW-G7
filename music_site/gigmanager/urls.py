from django.urls import path
from . import views

urlpatterns = [
    #URLS
    path('inicio', views.inicio, name='main'),
    path('gbwye', views.despedida, name='gbwye'),
    path('grupo/<int:id_grupo>', views.grupo, name='grup'),
    path('sala/<int:id_sala>', views.sala, name='sal'),
    path('musico/<int:id_musico>', views.musico, name='muso'),
    
]
