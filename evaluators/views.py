# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from .models import TypesEvaluator
# Create your views here.

def viewEvaluator(request):
    title = 'Lista de Pares Evaluadores Institucionales'
    template = loader.get_template('view_evaluator.html')
    listEvaluator = TypesEvaluator.objects.filter(fknamecareer__description__icontains='Institucional')
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))