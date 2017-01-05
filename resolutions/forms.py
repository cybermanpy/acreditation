from django import forms

class FormSearchResolution(forms.Form):
    text = forms.CharField(label='Busqueda', error_messages={'required': 'Este campo es obligatorio'})