from django.db import models

# Create your models here.
#Clase Genero, posibilidad
    
class Musico(models.Model):   
    # Campo para la relación   
    nombre = models.CharField(max_length=40)   
    fecha_nacimiento = models.DateField()   # Es posible indicar un valor por defecto mediante 'default'  
    
class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100, blank = True, null=True)
    integrante = models.ForeignKey(Musico, on_delete=models.CASCADE, blank = True, null=True)

class Sitio(models.Model):
    nombre = models.CharField(max_length=40)
    aforo = models.IntegerField(blank = True, null=True)
    direccion = models.CharField(max_length=100, blank = True, null=True)

#A futuro:

#Evento < para embellecer las funcionalidades
#Integrante < relaciona Musico y Grupo, se puede pillar el nombre del grupo en el que esta con la relacion.