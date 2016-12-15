# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from .models import TypeEvaluator
# Create your views here.

def viewEvaluator(request):
    title = 'Lista de Pares Evaluadores Institucionales'
    template = loader.get_template('view_evaluator.html')
    listEvaluator = TypeEvaluator.objects.filter(fknamecareer__description__icontains='Institucional')
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))