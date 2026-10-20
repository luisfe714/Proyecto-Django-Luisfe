"""
URL configuration for ProyectoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from mainapp import views #importamos el views que es el fichero de las vistas

import pages.views

urlpatterns = [
    path('admin/', admin.site.urls), #panel de administracion por defecto
    path('', views.index, name="index"), #configuracion de ruta vacia vinculada al index
    path('inicio/', views.index, name="inicio"),#Cuando encuentra la ruta inicio
    #path('nosotros/', views.about, name="about")#Creamos la url para about
    path('pagina/<str:slug>', pages.views.page, name="page"), #Pagina
]
