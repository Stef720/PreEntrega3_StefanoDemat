from django import forms
from Clase.models import Estudiante, Profesor, Curso, Comision

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre']  # Agrega otros campos aquí

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre']  # Agrega otros campos aquí

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre']  # Agrega otros campos aquí

# class ComisionForm(forms.ModelForm):
#     class Meta:
#         model = Comision
#         fields = ['nombre']  # Agrega otros campos aquí
#         fields = ['curso'] 
#         fields = ['profesor'] 
#         fields = ['estudiantes'] 