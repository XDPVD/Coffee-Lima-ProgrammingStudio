from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from IndieWorks.Apps.Cliente.forms import ClienteForm, ClienteUserForm

# Create your views here.


class ClienteLogin(HttpRequest):

    def login(request):
        return render(request, "login.html")

    def autenticarLogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")

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
        mensaje = "NOT OK"

        if cliente_form.is_valid() and cliente_user_form.is_valid():
            cliente_i = cliente_form.save(commit=False)
            user_i = cliente_user_form.save(commit=False)
            user_i.username = cliente_i.correo

            try:
                user = User.objects.get(username=user_i.username)
            except User.DoesNotExist:
                user = None

            if user is None:
                user_i.save()
                cliente_user_form.save_m2m()
                cliente_i.cuenta = user_i
                cliente_i.save()
                cliente_form.save_m2m()

                messages.success(request, "¡Se ha registrado de forma exitosa!")
                return redirect("login")

            cliente_form = ClienteForm()
            cliente_user_form = ClienteUserForm()

        diccionario = {"cliente": cliente_form, "user": cliente_user_form, "mensaje": mensaje}
        return render(request, "registro.html", diccionario)