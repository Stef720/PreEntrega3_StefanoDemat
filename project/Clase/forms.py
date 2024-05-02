from django import forms

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=100)
    
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)