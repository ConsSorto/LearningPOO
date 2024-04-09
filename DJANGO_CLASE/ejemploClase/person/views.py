from django.http import HttpResponse
from django.shortcuts import render

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


