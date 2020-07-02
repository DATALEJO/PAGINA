from django import forms

class FormularioContacto(forms.Form):
    
    name=forms.CharField()
    email=forms.EmailField()
    msg=forms.CharField()