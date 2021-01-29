from django.http import HttpRequest
from django.shortcuts import render

from IndieWorks.Apps.Cliente.forms import ClienteForm, ClienteUserForm

# Create your views here.

class ClienteLogin():

    def login(request):
        return render(request, "login.html")

class ClienteRegistro(HttpRequest):

    def registro(request):
        cliente_form = ClienteForm()
        cliente_user_form = ClienteUserForm()
        diccionario = {"cliente": cliente_form, "user": cliente_user_form}
        return render(request, "registro.html", diccionario)

    def procesarRegistro(request):
        cliente_form = ClienteForm(request.POST)
        cliente_user_form = ClienteUserForm(request.POST)
        mensaje = ""

        if (cliente_form.is_valid() and cliente_user_form.is_valid()):
            cliente_i = cliente_form.save(commit=False)
            user_i = cliente_user_form.save(commit=False)
            user_i.username = cliente_i.nombre
            user_i.save()
            cliente_user_form.save_m2m()
            cliente_i.cuenta = user_i
            cliente_i.save()
            cliente_form.save_m2m()

            cliente_form = ClienteForm()
            cliente_user_form = ClienteUserForm()
            mensaje = "OK"

        diccionario = {"cliente": cliente_form, "user": cliente_user_form, "mensaje": mensaje}
        return render(request, "registro.html", diccionario)