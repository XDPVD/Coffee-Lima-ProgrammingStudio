from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from IndieWorks.Apps.Trabajador.forms import TrabajadorForm, TrabajadorUserForm

# Create your views here.


class TrabajadorRegistro(HttpRequest):

    def registro(request):
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            trabajador_form = TrabajadorForm()
            trabajador_user_form = TrabajadorUserForm()
            diccionario = {"trabajador": trabajador_form, "user": trabajador_user_form}
            return render(request, "RegistroTrabajador.html", diccionario)

    def procesarRegistro(request):
        trabajador_form = TrabajadorForm(request.POST)
        trabajador_user_form = TrabajadorUserForm(request.POST)
        mensaje = "NOT OK"

        if trabajador_form.is_valid() and trabajador_user_form.is_valid():
            trabajador_i = trabajador_form.save(commit=False)
            user_i = trabajador_user_form.save(commit=False)
            user_i.username = trabajador_i.correo

            try:
                user = User.objects.get(username=user_i.username)
            except User.DoesNotExist:
                user = None

            if user is None:
                user_i.save()
                trabajador_user_form.save_m2m()

                trabajador_i.cuenta = user_i
                trabajador_i.apellido_paterno = trabajador_form.cleaned_data.get('apellido').split()[0]
                trabajador_i.apellido_materno = trabajador_form.cleaned_data.get('apellido').split()[1]
                trabajador_i.save()
                trabajador_form.save_m2m()

                messages.success(request, "¡Se ha registrado de forma exitosa!")
                return redirect("login")

            trabajador_form = TrabajadorForm()
            trabajador_user_form = TrabajadorUserForm()

        diccionario = {"cliente": trabajador_form, "user": trabajador_user_form, "mensaje": mensaje}
        return render(request, "RegistroTrabajador.html", diccionario)
