from django import forms

class BusquedaForm(forms.Form):
    nombre = forms.CharField(required=False)
    profesor = forms.CharField(required=False)
    curso = forms.CharField(required=False)
    # comision = forms.CharField(required=False)