from django import forms
from .models import Evaluator, TypesEvaluator
from statuses.models import Status
from django.db.models import Q

class EvaluatorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluatorForm, self).__init__(*args, **kwargs)
        self.fields['fkstatus'].queryset = Status.objects.filter(Q(description='Activo') | Q(description='Inactivo'))

    class Meta:
        model = Evaluator
        fields = ['firstname', 'lastname', 'fkresolution', 'curriculum', 'fkstatus', ]
        # exclude = ['typesevaluators', ]

class TypeEvaluatorForm(forms.ModelForm):
    class Meta:
        model = TypesEvaluator
        fields = ('__all__')


# class MyModelForm(forms.ModelForm):
#     def __init__(self, request, *args, **kwargs):
#         # request is a required parameter for this form.
#         super(MyModelForm, self).__init__(*args, **kwargs)
#         self.fields['website'].queryset = Website.objects.filter(organization__primary_account=request.user)