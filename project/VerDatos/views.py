from django.shortcuts import render
from .forms import BusquedaForm
from Clase.models import Estudiante, Profesor, Curso, Comision

def buscarEstudiante(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            # Realiza la búsqueda en la base de datos
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
            # Puedes agregar más filtros según tus necesidades
            return render(request, 'resultados.html', {'Estudiantes': estudiantes})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

def buscarProfesor(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            # Realiza la búsqueda en la base de datos
            profesores = Profesor.objects.filter(nombre__icontains=nombre)
            # Puedes agregar más filtros según tus necesidades
            return render(request, 'resultados.html', {'profesores': profesores})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

def buscarCurso(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            # Realiza la búsqueda en la base de datos
            cursos = Curso.objects.filter(nombre__icontains=nombre)
            # Puedes agregar más filtros según tus necesidades
            return render(request, 'resultados.html', {'cursos': cursos})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

# def buscarComision(request):
#     if request.method == 'POST':
#         form = BusquedaForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data['nombre']
#             # Realiza la búsqueda en la base de datos
#             comisiones = Comision.objects.filter(nombre__icontains=nombre)
#             # Puedes agregar más filtros según tus necesidades
#             return render(request, 'resultados.html', {'comisiones': comisiones})
#     else:
#         form = BusquedaForm()
#     return render(request, 'buscar.html', {'form': form})