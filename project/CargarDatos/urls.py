from django.urls import path
from .views import cargar_estudiante, cargar_profesor, cargar_curso #, cargar_comision

# Create your views here.

def home(request):
    ...
    
urlpatterns = [
     path('cargar_estudiante/', cargar_estudiante, name='cargar_estudiante'),
     path('cargar_profesor/', cargar_profesor, name='cargar_profesor'),
     path('cargar_curso/', cargar_curso, name='cargar_curso'),
     # path('cargar_comision/', cargar_comision, name='cargar_comision'),
 ]