# from django.forms import ModelForm
from universities.models import University
from django import forms

# class FormUniversity(ModelForm):
#     class Meta:
#         model = University
#         exclude = ['id']

class FormUniversity(forms.Form):
    university = forms.ModelMultipleChoiceField(queryset=University.objects.all())