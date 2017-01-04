# coding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TypesEvaluator, Evaluator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import EvaluatorForm, TypeEvaluatorForm, FormSearchIns, FormSearchDegree
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
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
def viewEvaluatorDegree(request):
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

def searchInstitutional(request):
    title = 'Pares Institucionales'
    label = 'institutional'
    template = loader.get_template('searchevaluator_list.html')
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearchIns(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__firstname__icontains=search,  fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo')
            elif options == '2':
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__lastname__icontains=search,  fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo')
            context = {
                'title': title,
                'label': label,
                'typesEvaluatorList': typesEvaluatorList,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchIns()
    typesEvaluatorList = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo')
    context = {
        'title': title,
        'label': label,
        'typesEvaluatorList': typesEvaluatorList,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def searchDegree(request):
    title = 'Pares Evaluadores de Carreras de Grado'
    label = 'degree'
    template = loader.get_template('searchevaluator_list.html')
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if request.method == 'POST':
        form = FormSearchDegree(request.POST)
        if form.is_valid():
            search = request.POST['text']
            options = request.POST['options']
            request.session['s_text'] = search
            request.session['s_options'] = options
            if options == '1':
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__firstname__icontains=search, fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
            elif options == '2':
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__lastname__icontains=search, fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
            elif options == '3':
                typesEvaluatorList = TypesEvaluator.objects.filter(fknamecareer__description__icontains=search, fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
            context = {
                'title': title,
                'label': label,
                'typesEvaluatorList': typesEvaluatorList,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchDegree()
    typesEvaluatorList = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
    context = {
        'title': title,
        'label': label,
        'typesEvaluatorList': typesEvaluatorList,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def cleanner(request, link):
    request.session['s_text'] = ''
    request.session['s_options'] = ''
    if link == 'institutional':
        url = 'evaluators:searchInstitutional'
        return redirect(reverse(url))
    elif link == 'degree':
        url = 'evaluators:searchDegree'
        return redirect(reverse(url))

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
