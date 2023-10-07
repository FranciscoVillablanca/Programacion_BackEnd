"""
URL configuration for Django_Evaluacion_1 project.

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
from Django_Evaluacion_1APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('alimentos/', views.alimentos),
    path('camas/', views.camas),
    path('juguetes/', views.juguetes),
    path('remedios/', views.remedios),
    path('alimentos/alimento1/', views.alimento1),
    path('alimentos/alimento2/', views.alimento2),
    path('alimentos/alimento3/', views.alimento3),
    path('camas/cama1/', views.cama1),
    path('camas/cama2/', views.cama2),
    path('camas/cama3/', views.cama3),
    path('juguetes/juguete1/', views.juguete1),
    path('juguetes/juguete2/', views.juguete2),
    path('juguetes/juguete3/', views.juguete3),
    path('remedios/remedio1/', views.remedio1),
    path('remedios/remedio2/', views.remedio2),
    path('remedios/remedio3/', views.remedio3)
]