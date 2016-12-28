# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from .models import TypesEvaluator, Evaluator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def viewEvaluator(request):
    title = 'Pares Evaluadores Institucionales'
    template = loader.get_template('view_evaluator.html')
    listEvaluator = TypesEvaluator.objects.filter(fknamecareer__description__icontains='Institucional')
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))

class EvaluatorList(ListView):
    model = Evaluator

class EvaluatorDetail(DetailView):
    model = Evaluator