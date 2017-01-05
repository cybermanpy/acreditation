from django import forms
from .models import NameCareer

class NameCareerForm(forms.ModelForm):
    class Meta:
        model = NameCareer
        fields = ('__all__')

class FormSearchNameCareer(forms.Form):
    text = forms.CharField(label='Busqueda', error_messages={'required': 'Este campo es obligatorio'})