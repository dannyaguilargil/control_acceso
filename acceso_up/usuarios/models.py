from django.db import models


class usuario(models.Model):
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento'),
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula'),
    nombre = models.CharField(max_length=40, verbose_name='Nombre'),
    apellido = models.CharField(max_length=40, verbose_name='Apellidos'),
    email = models.CharField(max_length=40, verbose_name='Email'),
    telefono = models.CharField(max_length=40, verbose_name='Telefono'),
    rol = models.CharField(max_length=40, verbose_name='Rol'),
    programa = models.CharField(max_length=40, verbose_name='Programa'),
    facultad = models.CharField(max_length=40, verbose_name='Facultad'),
    sexo = models.CharField(max_length=40, verbose_name='Sexo'),
    caducidad = models.CharField(max_length=40, verbose_name='Caducidad'),
    aula = models.CharField(max_length=40, verbose_name='Aula'),