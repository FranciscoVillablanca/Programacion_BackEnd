from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "TemplateAPP/index.html")

def alimentos(request):
    data = {"nombre": "Alimentos", "foto1":"alimento1.png", "foto2":"alimento2.png", "foto3":"alimento3.png", "producto1":"JOSERA NATURECAT", "producto2":"EUKANUBA TOP CONDITION", "producto3":"HILL'S METABOLIC + URINARY STRESS"}
    return render(request, "TemplateAPP/alimentos.html", data)

def camas(request):
    data2 = {"nombre": "Camas", "foto1":"cama1.jpg", "foto2":"cama2.jpg", "foto3":"cama3.jpg", "producto1":"CAMA IKEA PARA GATOS", "producto2":"CAMA TIPO IGLÚ PARA GATOS", "producto3":"CAMA TIPO SACO DE DORMIR PARA GATOS"}
    return render(request, "TemplateAPP/camas.html", data2)

def juguetes(request):
    data3 = {"nombre": "Juguetes", "foto1":"juguete1.jpg", "foto2":"juguete2.jpg", "foto3":"juguete3.jpg", "producto1":"EL JUGUETE 3 EN 1: JUGUETES INTERACTIVOS PARA GATOS DE LEAWRAY", "producto2":"PARA ENTRENAR LA MOVILIDAD: TÚNEL CON FORMA DE 'Y' PARA GATOS", "producto3":"PARA REDUCIR EL ESTRÉS: NEPFAIVY JUGUETES PEZ PARA GATOS"}
    return render(request, "TemplateAPP/juguetes.html", data3)

def remedios(request):
    data4 = {"nombre": "Remedios", "foto1":"medicina1.jpg", "foto2":"medicina2.jpg", "foto3":"medicina3.jpg", "producto1":"CEFOVECINA SÓDICA", "producto2":"DOXICILINA CALOX", "producto3":"DRAGXICILINA"}
    return render(request, "TemplateAPP/remedios.html", data4)

def alimento1(request):
    return render(request, "TemplateAPP/alimento1.html")

def alimento2(request):
    return render(request, "TemplateAPP/alimento2.html")

def alimento3(request):
    return render(request, "TemplateAPP/alimento3.html")

def cama1(request):
    return render(request, "TemplateAPP/cama1.html")

def cama2(request):
    return render(request, "TemplateAPP/cama2.html")

def cama3(request):
    return render(request, "TemplateAPP/cama3.html")

def juguete1(request):
    return render(request, "TemplateAPP/juguete1.html")

def juguete2(request):
    return render(request, "TemplateAPP/juguete2.html")

def juguete3(request):
    return render(request, "TemplateAPP/juguete3.html")

def remedio1(request):
    return render(request, "TemplateAPP/remedio1.html")

def remedio2(request):
    return render(request, "TemplateAPP/remedio2.html")

def remedio3(request):
    return render(request, "TemplateAPP/remedio3.html")

