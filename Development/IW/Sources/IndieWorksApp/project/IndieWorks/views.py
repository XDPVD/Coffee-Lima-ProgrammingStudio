from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


class Inicio(HttpRequest):

    def index(request):
        return render(request, "inicio.html")
