from django.db import models

# Create your models here.
   

class Musico(models.Model):   
    # Campo para la relación   
    nombre = models.CharField(max_length=40)   
    fecha_nacimiento = models.DateField()   # Es posible indicar un valor por defecto mediante 'default'

class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    integrante = models.ForeignKey(Musico, on_delete=models.CASCADE)

class Sitio(models.Model):
    nombre = models.CharField(max_length=40)