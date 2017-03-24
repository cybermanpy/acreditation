from django import forms
from .models import Evaluator, TypesEvaluator, EvaluatorUniversity
from statuses.models import Status
from django.db.models import Q

class EvaluatorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluatorForm, self).__init__(*args, **kwargs)
        self.fields['fkstatus'].queryset = Status.objects.filter(Q(description='Activo') | Q(description='Inactivo'))

    class Meta:
        model = Evaluator
        fields = ['firstname', 'lastname', 'ci', 'email',  'curriculum', 'fkstatus', 'fknationality' ]
        # exclude = ['typesevaluators', ]

class TypeEvaluatorForm(forms.ModelForm):
    class Meta:
        model = TypesEvaluator
        fields = ('__all__')

class EvaluatorUniversityForm(forms.ModelForm):
    class Meta:
        model = EvaluatorUniversity
        fields = ('__all__')

MY_INSTITUTIONAL = (
    ('1', 'Nombre'),
    ('2', 'Apellido'),
    )

class FormSearchIns(forms.Form):
    text = forms.CharField(label='Busqueda', error_messages={'required': 'Este campo es obligatorio'})
    options = forms.ChoiceField(choices=MY_INSTITUTIONAL, widget=forms.RadioSelect, error_messages={'required': 'Este campo es obligatorio'})


MY_DEGREE = (
    ('1', 'Nombre'),
    ('2', 'Apellido'),
    ('3', 'Carrera'),
    )

class FormSearchDegree(forms.Form):
    text = forms.CharField(label='Busqueda', error_messages={'required': 'Este campo es obligatorio'})
    options = forms.ChoiceField(choices=MY_DEGREE, widget=forms.RadioSelect, error_messages={'required': 'Este campo es obligatorio'})

# class MyModelForm(forms.ModelForm):
#     def __init__(self, request, *args, **kwargs):
#         # request is a required parameter for this form.
#         super(MyModelForm, self).__init__(*args, **kwargs)
#         self.fields['website'].queryset = Website.objects.filter(organization__primary_account=request.user)