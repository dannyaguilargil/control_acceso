from django.db import models

# Create your models here.
class usuario(models.Model):
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento'),
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula'),
    nombre = models.CharField(max_length=40, verbose_name='Nombre'),
    programa = models.CharField(max_length=40, verbose_name='Programa'),
    email = models.CharField(max_length=40, verbose_name='Email'),
    telefono = models.CharField(max_length=40, verbose_name='Telefono'),
    rol = models.CharField(max_length=40, verbose_name='Rol'),
