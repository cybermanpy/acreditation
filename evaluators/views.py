# coding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TypesEvaluator, Evaluator, EvaluatorUniversity
from typeevaluators.models import TypeEvaluator
from namecareers.models import NameCareer
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import EvaluatorForm, TypeEvaluatorForm, EvaluatorUniversityForm, FormSearchIns, FormSearchDegree
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db import IntegrityError

@login_required(login_url='/login/')
def viewEvaluatorInstitutional(request):
    title = 'Pares Evaluadores Institucionales'
    template = loader.get_template('view_evaluator_institutional.html')
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
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__firstname__icontains=search, fkevaluator__fkstatus__description='Activo')
            elif options == '2':
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__lastname__icontains=search, fkevaluator__fkstatus__description='Activo')
            context = {
                'title': title,
                'listEvaluator': listEvaluator,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchIns()
    listPaginator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo')
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listEvaluator = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listEvaluator = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def viewEvaluatorDegree(request):
    title = 'Pares Evaluadores de Carreras de Grado'
    template = loader.get_template('view_evaluator_degree.html')
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
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo', fkevaluator__firstname__icontains=search)
            elif options == '2':
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo', fkevaluator__lastname__icontains=search)
            elif options == '3':
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo', fknamecareer__description__icontains=search)
            context = {
                'title': title,
                'listEvaluator': listEvaluator,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchDegree()
    listPaginator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Carreras de Grado', fkevaluator__fkstatus__description='Activo')
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listEvaluator = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listEvaluator = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def viewEvaluatorArcusur(request):
    title = 'Pares Evaluadores de Carreras de Grado Modelo Arcusur'
    template = loader.get_template('view_evaluator_degree.html')
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
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo', fkevaluator__firstname__icontains=search)
            elif options == '2':
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo', fkevaluator__lastname__icontains=search)
            elif options == '3':
                listEvaluator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo', fknamecareer__description__icontains=search)
            context = {
                'title': title,
                'listEvaluator': listEvaluator,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchDegree()
    listPaginator = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo')
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listEvaluator = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listEvaluator = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def viewEvaluator(request):
    title = 'Pares Evaluadores'
    template = loader.get_template('list_evaluator.html')
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
                listEvaluator = Evaluator.objects.filter(firstname__icontains=search)
            elif options == '2':
                listEvaluator = Evaluator.objects.filter(lastname__icontains=search)
            context = {
                'title': title,
                'listEvaluator': listEvaluator,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchIns()
    listPaginator = Evaluator.objects.all()
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listEvaluator = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listEvaluator = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listEvaluator': listEvaluator,
        'form': form,
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
        form = EvaluatorForm(request.POST, request.FILES, instance=ins)
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

# @login_required(login_url='/login/')
# def newTypeEvaluator(request):
#     title = 'Asignar tipo de par'
#     template = loader.get_template('new_typesevaluator.html')
#     if request.method == 'POST':
#         form = TypeEvaluatorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             url = 'userprofiles:dashboard'
#             return HttpResponseRedirect(reverse(url))
#     else:
#         form = TypeEvaluatorForm()
#     context = {
#         'title': title,
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))

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
    typesEvaluatorList = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Institucional', fkevaluator__fkstatus__description='Activo').order_by('fknamecareer__description')
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

def searchArcusur(request):
    title = 'Pares Evaluadores de Carreras de Grado Modelo Arcusur'
    label = 'arcusur'
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
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__firstname__icontains=search, fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo')
            elif options == '2':
                typesEvaluatorList = TypesEvaluator.objects.filter(fkevaluator__lastname__icontains=search, fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo')
            elif options == '3':
                typesEvaluatorList = TypesEvaluator.objects.filter(fknamecareer__description__icontains=search, fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo')
            context = {
                'title': title,
                'label': label,
                'typesEvaluatorList': typesEvaluatorList,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchDegree()
    typesEvaluatorList = TypesEvaluator.objects.filter(fktypeevaluator__description__icontains='Arcusur', fkevaluator__fkstatus__description='Activo')
    context = {
        'title': title,
        'label': label,
        'typesEvaluatorList': typesEvaluatorList,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def newEvaluatorInstitutional(request, label, user):
    template = loader.get_template('new_typesevaluator.html')
    if request.method == 'POST':
        if label == '1':
            title = 'Agregar como par de carreras de grado'
            form = TypeEvaluatorForm(request.POST)
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.exclude(description='Institucional')
        elif label == '2':
            title = 'Agregar como par institucional'
            form = TypeEvaluatorForm(request.POST)
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.filter(description='Institucional')
        elif label == '3':
            title = 'Agregar como par de carreras de grado modelo ARCUSUR'
            form = TypeEvaluatorForm(request.POST)
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.exclude(description='Institucional')
        if form.is_valid():
            form.save()
            if label == '1':
                url = 'evaluators:degree'
            elif label == '2':
                url = 'evaluators:institutional'
            elif label == '3':
                url = 'evaluators:arcusur'
            return HttpResponseRedirect(reverse(url))
        else:
            if label == '1':
                error = 'El par evaluador ya pertenece a esa carrera'
            elif label == '2':
                error = "El par evaluador ya es institucional"
            elif label == '3':
                error = "El par evaluador ya pertence al modelo ARCUSUR"
            contextError = {
                'title': title,
                'error': error,
                'form': form,
            }
            return HttpResponse(template.render(contextError, request))            
    else:
        if label == '1':
            title = 'Agregar como par de carreras de grado'
            form = TypeEvaluatorForm()
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.exclude(description='Institucional')
        elif label == '2':
            title = 'Agregar como par institucional'
            form = TypeEvaluatorForm()
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.filter(description='Institucional')
        elif label == '3':
            title = 'Agregar como par de carreras de grado modelo ARCUSUR'
            form = TypeEvaluatorForm()
            form.fields['fktypeevaluator'].queryset = TypeEvaluator.objects.filter(id=label)
            form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
            form.fields['fknamecareer'].queryset = NameCareer.objects.exclude(description='Institucional')
    context = {
        'title': title,
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
    elif link == 'arcusur':
        url = 'evaluators:searchArcusur'
        return redirect(reverse(url))


@login_required(login_url='/login/')
def viewDeclaration(request):
    title = 'Declaraciones'
    template = loader.get_template('view_declaration.html')
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
                listDeclaration = EvaluatorUniversity.objects.filter(fkevaluator__fkstatus__description='Activo', fkevaluator__firstname__icontains=search)
            elif options == '2':
                listDeclaration = EvaluatorUniversity.objects.filter(fkevaluator__fkstatus__description='Activo', fkevaluator__lastname__icontains=search)
            context = {
                'title': title,
                'listDeclaration': listDeclaration,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearchIns()
    listPaginator = EvaluatorUniversity.objects.filter(fkevaluator__fkstatus__description='Activo')
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listDeclaration = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listDeclaration = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listDeclaration': listDeclaration,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
# def newDeclaration(request):
#     title = 'Agregar nueva declaracion'
#     template = loader.get_template('new_declaration.html')
#     if request.method == 'POST':
#         form = EvaluatorUniversityForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             url = 'evaluators:viewDeclaration'
#             return HttpResponseRedirect(reverse(url))
#         else:
#             error = 'La declaración esta duplicada'
#             contextError = {
#                 'title': title,
#                 'error': error,
#                 'form': form,
#             }
#             return HttpResponse(template.render(contextError, request))
#     else:
#         form = EvaluatorUniversityForm()
#     context = {
#         'title': title,
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def newDeclaration(request, user):
    title = 'Agregar nueva declaracion'
    template = loader.get_template('new_declaration.html')
    if request.method == 'POST':
        form = EvaluatorUniversityForm(request.POST, request.FILES)
        form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
        if form.is_valid():
            form.save()
            url = 'evaluators:viewDeclaration'
            return HttpResponseRedirect(reverse(url))
        else:
            error = 'La declaración esta duplicada'
            contextError = {
                'title': title,
                'error': error,
                'form': form,
            }
            return HttpResponse(template.render(contextError, request))
    else:
        form = EvaluatorUniversityForm()
        form.fields['fkevaluator'].queryset = Evaluator.objects.filter(id=user)
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def editDeclaration(request, pk):
    title = 'Actualizar declaración'
    template = loader.get_template('new_declaration.html')
    ins = get_object_or_404(EvaluatorUniversity, pk=pk)
    if request.method == 'POST':
        form = EvaluatorUniversityForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            url = 'evaluators:viewDeclaration'
            return HttpResponseRedirect(reverse(url))
        else:
            error = 'La declaración esta duplicada'
            contextError = {
                'title': title,
                'error': error,
                'form': form,
            }
            return HttpResponse(template.render(contextError, request))
    else:
        form = EvaluatorUniversityForm(instance=ins)
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
