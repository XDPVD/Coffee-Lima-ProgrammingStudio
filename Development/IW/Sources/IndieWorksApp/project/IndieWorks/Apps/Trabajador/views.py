from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from .models import Trabajador
from django.shortcuts import get_object_or_404
from .forms import TrabajadorForm, TrabajadorUserForm

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


def busquedaTrabInd(request):
    
    datosForm = request.POST
    #Solicitar lista de trabajadores independientes
    if bool(datosForm) and datosForm.get('fname') != "":
        nombreBuscar = datosForm.get('fname') #Obtención del campo nombre
        #Busqueda de trabajadores que contengan en su nombre el campo ingresado
        idBuscados = [ti.id for ti in Trabajador.objects.all()  if nombreBuscar in ti.NombreCompleto() or nombreBuscar in ti.NombreCompleto().lower()]
        #Lista de trabajadores con similitudes
        trabajadores = Trabajador.objects.filter(id__in=idBuscados)
    else:
        return redirect('../inicio/')

    #Carga de la lista en el contexto
    contexto = {}
    contexto["listaTrabajadores"] = trabajadores
    contexto["nombreBuscAnterior"] = nombreBuscar
    contexto["usuario"] = request.user

    print("Usuario: ",contexto["usuario"])
    print(request.user.is_anonymous)

    import sys
    sys.stdin.flush()

    #renderizado del html
    return render(request,"lista-ti.html",contexto)

def detalleTrabajador(request,id):
    
    #Solicitar información del trabajador
    trabajador = get_object_or_404(Trabajador, id=id)

    #Cargar el contexto
    context ={}
    context["trabajador"] = trabajador
    context["usuario"] = request.user

    print("Usuario: ",context["usuario"])
    print(request.user.is_anonymous)

    import sys
    sys.stdin.flush()

    #renderizar
    return render(request,"detalle-trabajador.html",context)