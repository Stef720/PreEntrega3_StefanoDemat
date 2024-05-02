from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Curso, Profesor, Estudiante
from .forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario

from . import models

# Create your views here.

def menu(request):
      return render(request, 'core/index.html')

def home(request):
    query = models.Comision.objects.all()
    context = {'comisiones': query}
    return render(request, 'Clase/index.html', context)

def curso(request):
      return render(request, "Clase/cursos.html")

def estudiante(request):
      return render(request, "Clase/estudiantes.html")

def comisiones(request):
      return render(request, "Clase/comisiones.html")

def cursos(request):
      if request.method == 'POST':
            miFormulario = CursoFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso (nombre=informacion['nombre']) 
                  curso.save()
                  return render(request, "Clase/index.html")
      else: 
            miFormulario= CursoFormulario()
      return render(request, "Clase/cursos.html", {"miFormulario":miFormulario})


def profesores(request):
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor (nombre=informacion['nombre']) 
                  profesor.save()
                  return render(request, "Clase/index.html")
      else: 
            miFormulario= ProfesorFormulario()
      return render(request, "Clase/profesores.html", {"miFormulario":miFormulario})
  
def estudiantes(request):
      if request.method == 'POST':
            miFormulario = EstudianteFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante (nombre=informacion['nombre']) 
                  estudiante.save()
                  return render(request, "Clase/index.html")
      else: 
            miFormulario= ProfesorFormulario()
      return render(request, "Clase/profesores.html", {"miFormulario":miFormulario})
  
def buscar(request):
      if  request.GET["comisiones"]:
            comisiones = request.GET['comisiones'] 
            cursos = Curso.objects.filter(comisiones__icontains=comisiones)
            return render(request, "Clase/index.html", {"comisiones":comisiones})
      else: 
	      respuesta = "No pediste datos"
      return HttpResponse(respuesta)