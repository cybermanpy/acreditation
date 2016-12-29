from django import forms
from .models import Evaluator, TypesEvaluator

class EvaluatorForm(forms.ModelForm):
    class Meta:
        model = Evaluator
        fields = ['firstname', 'lastname', 'fkresolution', 'curriculum', 'fkstatus', ]
        exclude = ['typesevaluators', ]

class TypeEvaluatorForm(forms.ModelForm):
    class Meta:
        model = TypesEvaluator
        fields = ('__all__')