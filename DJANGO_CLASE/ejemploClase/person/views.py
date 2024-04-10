from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
# Create your views here.
def ejemplo(request):
    return HttpResponse("Ejemplo en clase")

def ejemploPersona(request, persona):
    return HttpResponse("Ejemplo en clase " + persona)

def ejemploPersona2(request, persona, apellido = ""):
    return HttpResponse("Ejemplo en clase " + persona + " " + apellido)


def ejemploRender(request):
    return render(request, "ejemplo.html")

def ejemploRenderVar(request):
    return render(request, "ejemplovar.html",
                  {'title': 'Paso Variables', 'contenido': 'El contenido es paso de variables'})

def ejemploRenderIfFor(request):
    numeros = range(0,11)
    return render(request, "iffor.html", {'numeros': numeros})


def ejemploRenderLayout(request):
    return render(request, "usoPlantilla.html")

def index(request):
    personas = Person.objects.all()
    return render(request, "personas.html"
                  , {'title':'Listado Personas', 'personas': personas})

