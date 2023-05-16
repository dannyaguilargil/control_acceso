from django.db import models

# Create your models here.
class equipo(models.Model):
    serial = models.CharField(primary_key=True,  max_length=40, verbose_name='Serial'),
    placa = models.CharField(max_length=40, verbose_name='Placa'),
    sistema = models.CharField(max_length=40, verbose_name='Sistema'),
    marca = models.CharField(max_length=40, verbose_name='Marca'),
    codigo = models.CharField(max_length=40, verbose_name='Codigo'),
    equipo = models.CharField(max_length=40, verbose_name='Equipo'),
    procesador = models.CharField(max_length=40, verbose_name='Procesador'),
    ram = models.CharField(max_length=40, verbose_name='Ram'),
    discoduro = models.CharField(max_length=40, verbose_name='Disco duro'),
    monitor = models.CharField(max_length=40, verbose_name='Monitor'),
    monitorserial = models.CharField(max_length=40, verbose_name='Serial del monitor'),
    monitorcaracteristicas = models.CharField(max_length=40, verbose_name='Caracteristicas del monitor'),
    teclado = models.CharField(max_length=40, verbose_name='Teclado'),
    tecladoserial = models.CharField(max_length=40, verbose_name='Serial del teclado'),
    tecladocaracteristicas = models.CharField(max_length=40, verbose_name='Caracteristicas del teclado'),
    mouse = models.CharField(max_length=40, verbose_name='Mouse'),
    mouseserial = models.CharField(max_length=40, verbose_name='Serial del mouse'),
    mousecaracteristicas = models.CharField(max_length=40, verbose_name='Caracteristicas del mouse'),
    observaciones = models.CharField(max_length=40, verbose_name='Observaciones'),

