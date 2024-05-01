from django.urls import path
from .views import buscarEstudiante, buscarCurso, buscarProfesor

app_name = 'VerDatos'

# urlpatterns = [
#     #path('', views.home, name='home'),
# ]

urlpatterns = [
    path('buscarEstudiante/', buscarEstudiante, name='Buscar Estudiante'),
    path('buscarProfesor/', buscarProfesor, name='Buscar Profesor'),
    path('buscarCurso/', buscarCurso, name='Buscar Curso'),
]
