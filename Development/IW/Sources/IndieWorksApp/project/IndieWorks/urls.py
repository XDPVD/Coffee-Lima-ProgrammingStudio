"""IndieWorks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from IndieWorks.views import Inicio
from IndieWorks.Apps.Cliente.views import ClienteLogin, ClienteRegistro
from IndieWorks.Apps.Trabajador.views import TrabajadorRegistro

urlpatterns = [
    path('admin/', admin.site.urls),

    path('inicio/', Inicio.index, name="inicio"),

    path('login/', ClienteLogin.login, name="login"),
    path('login_auth/', ClienteLogin.autenticarLogin, name="login_auth"),
    path('registroc/', ClienteRegistro.registro, name="cliente_registro"),
    path('registroc_resultado/', ClienteRegistro.procesarRegistro,
         name="cliente_registro_resultado"),
    path('registrot/', TrabajadorRegistro.registro, name="trabajador_registro"),
    path('registrot_resultado/', TrabajadorRegistro.procesarRegistro,
         name="trabajador_registro_resultado")
    path('mostrar_ti/', )
]
