from django.urls import path
from . import views

urlpatterns = [
    #URLS
    path('', views.index, name='index'),
    
]
