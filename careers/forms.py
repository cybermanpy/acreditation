# from django.forms import ModelForm
# from universities.models import University
from django import forms

# class FormUniversity(ModelForm):
#     class Meta:
#         model = University
#         exclude = ['id']

MY_CHOICES = (
    ('1', 'Carrera'),
    ('2', 'Universidad'),
    ('3', 'Facultad'),
    )

class FormSearch(forms.Form):
    text = forms.CharField(label='Busqueda', error_messages={'required': 'Este campo es obligatorio'})
    options = forms.ChoiceField(choices=MY_CHOICES, widget=forms.RadioSelect, error_messages={'required': 'Este campo es obligatorio'})

# class FormUniversity(forms.Form):
#     university = forms.ModelMultipleChoiceField(queryset=University.objects.all(), error_messages={'required': 'Debe ingresar una universidad'})