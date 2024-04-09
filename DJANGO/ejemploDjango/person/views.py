from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

# Create your views here.

def infoperson(request):
    return HttpResponse("Esto es un ejemplo")


def mensaje(request, mensaje):
    return HttpResponse(mensaje)

def mensajePersona(request, mensaje, persona = ""):
    return HttpResponse(mensaje + " " + persona)


def respuestaRender(request):
    return render(request, "index.html")

def respuestaRenderVariables(request):
    return render(request, "variables.html", {"title": "Esto es una pag con variables"
        , "header":"Esta es la variable header"})

def respuestaRenderLayout(request):
    return render(request, "useLayout.html")

def respuestaRenderIfFor(request):
    numeros = range(0,11)
    title = "Pagina de numeros"
    return render(request, "useIfFor.html", {"numeros":numeros, "title":title})

#################### CRUD #########################################

def personsIndex(request):
    persons = Person.objects.all()
    return render(request, "persons.html",
                  {'title': 'Listado de persona', 'persons': persons})

