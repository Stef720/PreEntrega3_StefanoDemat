from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm, CursoForm #, ComisionForm

# Create your views here.

def home(request):
    ...

def cargar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargar_estudiante')
    else:
        form = EstudianteForm()
    return render(request, 'cargar_estudiante.html', {'form': form})

def cargar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargar_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'cargar_profesor.html', {'form': form})

def cargar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargar_curso')
    else:
        form = CursoForm()
    return render(request, 'cargar_curso.html', {'form': form})

# def cargar_comision(request):
#     if request.method == 'POST':
#         form = ComisionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cargar_comision')
#     else:
#         form = ComisionForm()
#     return render(request, 'cargar_comision.html', {'form': form})