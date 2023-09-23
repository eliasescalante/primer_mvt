from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    