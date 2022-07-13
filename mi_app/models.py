from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    es = models.CharField(max_length=40)
   
class Curso(models.Model):
    
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()

   def __str__(self):
       return f"{self.nombre}  {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=255)  
