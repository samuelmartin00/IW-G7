from django.db import models

# Create your models here.
   

class Musico(models.Model):   
    # Campo para la relación   
    nombre = models.CharField(max_length=40)   
    fecha_nacimiento = models.DateField()   # Es posible indicar un valor por defecto mediante 'default'

class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    lider = models.ForeignKey(Musico, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

class Integrante(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Sitio(models.Model):
    nombre = models.CharField(max_length=40)
    aforo = models.IntegerField(blank = True, null=True)