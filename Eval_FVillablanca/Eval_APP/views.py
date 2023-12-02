from django.shortcuts import render, redirect
from .models import Socio
from .forms import SocioForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lista_socios(request):
    socios = Socio.objects.all()
    data =  {'socios': socios}
    return render(request, 'lista_socios.html', data)

def agregar_socio(request):
    form = SocioForm()

    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)

    data = {'form': form}
        
    return render(request, 'agregar_socios.html', data)

def modificar_socio(request, id):
    socio = Socio.objects.get(id=id)
    form = SocioForm(instance=socio)

    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('/lista_socios')

    data = {'form': form}
    return render(request, 'agregar_socios.html', data)

def eliminar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.delete()
    return redirect('/lista_socios')