from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Trabajador(models.Model):
    cuenta = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=35)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    dni = models.CharField(validators=[MinLengthValidator(8)], max_length=8)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(validators=[MinLengthValidator(7)], max_length=9)
    ruc = models.CharField(validators=[MinLengthValidator(10)], max_length=10)
    distrito = models.CharField(max_length=20)

    def NombreCompleto(self):
        cadena="{0} {1} {2}"
        return cadena.format(self.nombre, self.apellido_paterno, self.apellido_materno)

    def __str__(self):
        return self.NombreCompleto()

    def get_absolute_url(self):
        return reverse("detalle-trabajador", kwargs={"id": self.id})
    