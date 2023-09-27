from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("Hola, tardes buenas")

def infoTemplate(request):
    data = {"id":"123", "nombre":"Clark Kent", "email":"superman@jl.org"}
    return render(request, "TemplateAPP1/userInfoTemplate.html", data)