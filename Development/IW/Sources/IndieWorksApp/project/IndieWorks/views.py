from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect


# Create your views here.


class Login(HttpRequest):

    def loginUser(request):
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            return render(request, "index.html")

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


class Inicio(HttpRequest):

    @login_required(login_url='login')
    def index(request):
        return render(request, "index.html")

def nosotros(request):
    return render(request,"nosotros.html",{})