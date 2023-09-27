from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "TemplateAPP2/index.html")

def producto(request):
    data = {"nombre" : "Producto", "foto1":"camara.jpg", "foto2":"reloj.png", "foto3":"telefono.jpg", "producto1":"Camara Digital", "producto2":"Smartwatch", "producto3":"Smartphone"}
    return render(request, "TemplateAPP2/producto.html", data)

def juguetes(request):
    data2 = {"nombre" : "Juguetes", "foto1":"avion.png", "foto2":"figuras.png", "foto3":"lego.jpg", "producto1":"Aviones", "producto2":"Figuras", "producto3":"Armables"}
    return render(request, "TemplateAPP2/producto.html", data2)

def ropa(request):
    data3 = {"nombre" : "Ropa", "foto1":"falda.jpg", "foto2":"polera.png", "foto3":"vestido.png", "producto1":"Faldas", "producto2":"Poleras", "producto3":"Vestidos"}
    return render(request, "TemplateAPP2/producto.html", data3)
