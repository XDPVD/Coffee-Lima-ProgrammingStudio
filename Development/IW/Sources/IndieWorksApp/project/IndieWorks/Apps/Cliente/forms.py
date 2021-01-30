from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from IndieWorks.Apps.Cliente.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ['rating']


class ClienteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
