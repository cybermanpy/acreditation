# coding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TypesEvaluator, Evaluator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import EvaluatorForm, TypeEvaluatorForm
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='/login/')
def viewEvaluatorInstitutional(request):
    title = 'Pares Evaluadores Institucionales'
    template = loader.get_template('view_evaluator_institutional.html')
    listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo')
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def viewEvaluatorGrado(request):
    title = 'Pares Evaluadores de Carreras de Grado'
    template = loader.get_template('view_evaluator_grado.html')
    listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def viewEvaluator(request):
    title = 'Pares Evaluadores'
    template = loader.get_template('list_evaluator.html')
    listEvaluator = Evaluator.objects.all()
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def newEvaluator(request):
    title = 'Agregar nuevo par'
    template = loader.get_template('new_evaluator.html')
    if request.method == 'POST':
        form = EvaluatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = 'evaluators:evaluator'
            return HttpResponseRedirect(reverse(url))
    else:
        form = EvaluatorForm()
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def editEvaluator(request, pk):
    title = 'Actualizar par'
    template = loader.get_template('new_evaluator.html')
    ins = get_object_or_404(Evaluator,pk=pk)
    if request.method == 'POST':
        form = EvaluatorForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            url = 'evaluators:evaluator'
            return HttpResponseRedirect(reverse(url))
    else:
        form = EvaluatorForm(instance=ins)
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def newTypeEvaluator(request):
    title = 'Asignar tipo de par'
    template = loader.get_template('new_typesevaluator.html')
    if request.method == 'POST':
        form = TypeEvaluatorForm(request.POST)
        if form.is_valid():
            form.save()
            url = 'userprofiles:dashboard'
            return HttpResponseRedirect(reverse(url))
    else:
        form = TypeEvaluatorForm()
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def editTypeEvaluator(request, pk):
    title = 'Actualizar tipo par'
    template = loader.get_template('new_typesevaluator.html')
    ins = get_object_or_404(TypesEvaluator, pk=pk)
    if request.method == 'POST':
        form = TypeEvaluatorForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            url = 'userprofiles:dashboard'
            return HttpResponseRedirect(reverse(url))
    else:
        form = TypeEvaluatorForm(instance=ins)
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

class ListInstitutional(ListView):
    model = TypesEvaluator
    title = 'Pares Institucionales'

    def get_queryset(self):
        return TypesEvaluator.objects.filter(fknamecareer__description__icontains='Institucional')

class ListAgronomia(ListView):
    model = TypesEvaluator

    def get_queryset(self):
        return TypesEvaluator.objects.filter(fknamecareer__description__icontains='Ingeniería Agronómica')

class EvaluatorList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Evaluator

class EvaluatorDetail(DetailView):
    model = Evaluator


# template_name = 'loggedin_load/live_bids.html'