from django.db import models

# Create your models here.
#Clase Genero, posibilidad
class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100, blank = True, null=True)
    
class Musico(models.Model):   
    # Campo para la relación   
    nombre = models.CharField(max_length=40)   
    fecha_nacimiento = models.DateField()   # Es posible indicar un valor por defecto mediante 'default'
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank = True, null=True)   

class Sitio(models.Model):
    nombre = models.CharField(max_length=40)
    aforo = models.IntegerField(blank = True, null=True)
    direccion = models.CharField(max_length=100, blank = True, null=True)