from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()
    email = models.EmailField()

class Profesores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()