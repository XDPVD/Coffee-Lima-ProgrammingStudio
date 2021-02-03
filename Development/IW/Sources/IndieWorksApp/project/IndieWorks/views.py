from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from IndieWorks.Apps.Cliente.models import Cliente
from IndieWorks.Apps.Trabajador.models import Trabajador


# Create your views here.


class Inicio(HttpRequest):
    def index(request):
        conexion = ""
        usuario = None

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.get_username())
            trabajador = Trabajador.objects.filter(cuenta_id=user.id).first()

            if trabajador is None:
                usuario = Cliente.objects.get(cuenta_id=user.id)
                conexion = "cliente"
            else:
                usuario = trabajador
                conexion = "trabajador"

        diccionario = {"conexion": conexion, "usuario": usuario}
        return render(request, "Inicio.html", diccionario)


class Registro(HttpRequest):
    def registro(request):
        return render(request, "MenuRegistrar.html")


class Login(HttpRequest):

    def loginUser(request):
        print(request.user,flush=True)
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            return render(request, "Login.html")

    def autenticarLogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")

        return render(request, "Login.html")

    def logoutUser(request):
        logout(request)
        return redirect('login')
    
def nosotros(request):
    return render(request,"nosotros.html",{})
