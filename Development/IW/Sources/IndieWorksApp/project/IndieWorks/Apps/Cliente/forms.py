from django.contrib.auth.models import User
from django.forms import ModelForm

from IndieWorks.Apps.Cliente.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ['rating']


class ClienteUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']
