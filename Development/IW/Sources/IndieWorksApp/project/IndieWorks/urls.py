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

from .views import Inicio
from .Apps.Cliente.views import ClienteLogin, ClienteRegistro
from .Apps.Trabajador.views import TrabajadorRegistro, busquedaTrabInd, detalleTrabajador

urlpatterns = [
    path('admin/', admin.site.urls),

    path('inicio/', Inicio.index, name="inicio"),

    path('login/', Login.loginUser, name="login"),
    path('login_auth/', Login.autenticarLogin, name="login_auth"),
    path('logout/', Login.logoutUser, name="logout"),

    path('registroc/', ClienteRegistro.registro, name="cliente_registro"),
    path('registroc_resultado/', ClienteRegistro.procesarRegistro,
         name="cliente_registro_resultado"),
    path('registrot/', TrabajadorRegistro.registro, name="trabajador_registro"),
    << << << < HEAD
    path('registrot_resultado/', TrabajadorRegistro.procesarRegistro,
         name="trabajador_registro_resultado"),

    path('busqueda/', busquedaTrabInd, name="lista-trabajadores"),
    path('trabajador/<int:id>', detalleTrabajador, name="detalle-trabajador"),
    == == == =
    path('registrot_resultado/', TrabajadorRegistro.procesarRegistro,
         name="trabajador_registro_resultado")
    >> >>>> > edwinAguilar
]
