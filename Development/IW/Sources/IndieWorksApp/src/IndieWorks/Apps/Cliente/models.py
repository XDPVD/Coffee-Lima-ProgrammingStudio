from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=35)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    dni = models.DecimalField(max_digits=8)
    correo
