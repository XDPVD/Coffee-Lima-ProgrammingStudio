from django.forms import ModelForm

from IndieWorks.Apps.Servicio.models import Servicio


class ServicioForm(ModelForm):

    class Meta:
        model = Servicio
        exclude = ['cliente', 'trabajador', 'fecha', 'estado', 'rating']
