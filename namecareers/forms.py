from django import forms
from .models import NameCareer

class NameCareerForm(forms.ModelForm):
    class Meta:
        model = NameCareer
        fields = ('__all__')