from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from IndieWorks.Apps.Servicio.forms import ServicioForm
from IndieWorks.Apps.Servicio.models import Servicio
from IndieWorks.Apps.Trabajador.models import Trabajador
from django.db.models import Q
from operator import or_
from functools import reduce


# Create your views here.


class ServicioControlador(HttpRequest):

    def misServicios(request):
        return render(request, "MisServicios.html")

    def publicarServicio(request):
        servicio_form = ServicioForm()
        diccionario = {"servicio": servicio_form}
        return render(request, "PublicarServicio.html", diccionario)

    def procesarServicio(request):
        servicio_form = ServicioForm(request.POST)
        mensaje = "NOT OK"

        if servicio_form.is_valid():
            servicio_i = servicio_form.save(commit=False)
            user = User.objects.get(username=request.user.get_username())
            trabajador = Trabajador.objects.get(cuenta_id=user.id)
            servicio_i.trabajador = trabajador
            servicio_i.save()
            servicio_form.save_m2m()

            mensaje = "OK"

        servicio_form = ServicioForm()

        diccionario = {"servicio": servicio_form, "mensaje": mensaje}
        return render(request, "PublicarServicio.html", diccionario)

    def buscarServicio(request):
        if request.method == 'POST':
            servicio = request.POST.get('servicio')
            servicio_split = servicio.split()
            reduce_query = reduce(
                or_, (Q(nombre__icontains=x) for x in servicio_split))
            servicios = Servicio.objects.filter(reduce_query)
            print(servicios)
            return render(request, "lista-servicios.html", {'servicios': servicios})
