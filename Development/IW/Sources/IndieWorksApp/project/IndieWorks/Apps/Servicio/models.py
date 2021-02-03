from django.core.validators import MinLengthValidator
from django.db import models

from IndieWorks.Apps.Cliente.models import Cliente
from IndieWorks.Apps.Trabajador.models import Trabajador


# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    distrito = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=50)
    descripcion = models.TextField()
    telefono = models.CharField(validators=[MinLengthValidator(7)], max_length=9)
    categoria = models.CharField(max_length=15, null=False)
    precio = models.FloatField(default=0)
    fecha = models.DateField(auto_now_add=True)
    ESTADO_CHOICES = [
        ('1', 'Publicado'),
        ('2', 'Solicitado'),
        ('3', 'Terminado')
    ]
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='1')
    rating = models.FloatField(default=0)

    def NombreServicio(self):
        cadena = "{0} - {1}"
        return cadena.format(self.trabajador, self.categoria)

    def __str__(self):
        return self.NombreServicio()

