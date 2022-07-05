from django.db import models


class curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada= models.IntegerField()

class familia(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad= models.IntegerField()
    es= models.CharField(max_length=40)
  
