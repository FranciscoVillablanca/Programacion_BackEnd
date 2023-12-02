"""
URL configuration for Eval_FVillablanca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Eval_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('lista_socios/', views.lista_socios),
    path('agregar_socios/', views.agregar_socio),
    path('modificar_socio/<int:id>/', views.modificar_socio),
    path('eliminar_socio/<int:id>/', views.eliminar_socio)
]
