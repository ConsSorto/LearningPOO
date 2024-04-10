"""
URL configuration for ejemploClase project.

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
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('ejemplo/<str:persona>', views.ejemploPersona, name='ejemploPersona'),
    path('ejemplo/<str:persona>/<str:apellido>', views.ejemploPersona2, name='ejemploPersona2'),
    path('ejemplo-render', views.ejemploRender, name='ejemploRender'),
    path('ejemplo-render-var', views.ejemploRenderVar, name='ejemploRenderVar'),
    path('ejemplo-render-iffor', views.ejemploRenderIfFor, name='ejemploRenderIfFor'),
    path('ejemplo-render-uso-plantilla', views.ejemploRenderLayout, name='ejemploRenderLayout'),
    path('personas', views.index, name='personas'),

]
