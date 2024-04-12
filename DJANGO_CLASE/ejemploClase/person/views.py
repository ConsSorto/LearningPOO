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

def create(request):
    return render(request, "create.html"
                  , {'title':'Creacion'})

def save(request):

    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        person = Person(firstName = firstName, lastName = lastName)
        person.save()

    return index(request)

def get(request, pk):
    person = Person.objects.get(pk=pk)
    return render(request, 'person.html',
                 {'title' : 'Persona', 'persona':person})


def edit(request, pk):
    person = Person.objects.get(pk=pk)

    return render(request, 'edit.html',
                 {'title' : 'Editar', 'persona':person})

def update(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == "POST":
        person.firstName = request.POST['firstName']
        person.lastName = request.POST['lastName']
        person.save()

    return index(request)

def delete(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == "POST":
        person.delete()

    return index(request)