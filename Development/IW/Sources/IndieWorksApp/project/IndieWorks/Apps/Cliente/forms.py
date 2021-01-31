from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField

from IndieWorks.Apps.Cliente.models import Cliente


class ClienteForm(ModelForm):
    apellido = CharField(max_length=30)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'correo', 'telefono', 'distrito']
        # exclude = ['rating', 'apellido_paterno', 'apellido_materno']


class ClienteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
