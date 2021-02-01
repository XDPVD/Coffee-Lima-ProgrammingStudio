from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField

from IndieWorks.Apps.Trabajador.models import Trabajador


class TrabajadorForm(ModelForm):
    apellido = CharField(max_length=30)

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'dni', 'ruc', 'correo', 'telefono', 'distrito']


class TrabajadorUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']