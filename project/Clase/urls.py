from django.urls import path
from . import views

app_name = 'Clase'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('comisiones', views.comisiones, name="comisiones"),
    path('buscar/', views.buscar),
]
