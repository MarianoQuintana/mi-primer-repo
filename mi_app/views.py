from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Familia
from mi_app.models import Curso
from mi_app.models import Estudiante

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo { fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def saludo_personalizado(request):
    pass

def mostrar_index (request):
    return render(request, "mi_app/index.html", {"mi_titulo":"hola esta es mi primer website!!"})
    
   

def familia(request): 
    context = {}

    context["familiar"] = Familia.objects.all()
    return render(request,"mi_app/familia.html", context)
    
def curso(request): 
    context = {}

    context["cursos"] = Curso.objects.all()
    return render(request,"mi_app/lista_cursos.html", context)

def listar_estudiantes(request): 
    context = {}
    context["estudiantes"] = Estudiante.objects.all()   
    return render(request,"mi_app/lista_estudiantes.html", context)

