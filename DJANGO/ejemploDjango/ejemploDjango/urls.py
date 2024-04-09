"""
URL configuration for ejemploDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from person import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('infoperson/', views.infoperson, name='infoperson'),
    path('mensaje/<str:mensaje>', views.mensaje, name='mensaje'),
    path('mensaje/<str:mensaje>/<str:persona>', views.mensajePersona, name='mensajePersona'),
    path('', views.respuestaRender, name='respuestaRender'),
    path('variables/', views.respuestaRenderVariables, name='respuestaRenderVariables'),
    path('usoLayout/', views.respuestaRenderLayout, name='respuestaUseLayout'),
    path('usoIfFor/', views.respuestaRenderIfFor, name='respuestaRenderIfFor'),
    path('persons/index', views.personsIndex, name='personsIndex'),

]


