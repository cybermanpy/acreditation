# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Career
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from careers.forms import FormUniversity

# Create your views here.

# def viewCareers(request):
#     title = 'Carreras Acreditadas Modelo Nacional'
#     careers = Career.objects.all().order_by('national')
#     template = loader.get_template('view_careers.html')
#     context = {
#         'careers': careers,
#         'title':  title,
#     }
#     return HttpResponse(template.render(context, request))

def viewNational(request):
    title = 'Carreras de Grado Modelo Nacional'
    template = loader.get_template('view_careers.html')
    form = FormUniversity()
    listCareer = Career.objects.all().order_by('national')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def viewCareer(request):
    title = 'Carreras de Grado Acreditadas por Carreras'
    template = loader.get_template('view_careers.html')
    listCareer = Career.objects.all().order_by('fknamecareer__description')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
    }
    return HttpResponse(template.render(context, request))

def viewUniversity(request):
    title = 'Carreras de Grado Acreditadas por Universidad'
    template = loader.get_template('view_careers.html')
    listCareer = Career.objects.all().order_by('fkfaculty__fkuniversity__name')
    paginator = Paginator(listCareer, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        careers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        careers = paginator.page(paginator.num_pages)
    context = {
        'careers': careers,
        'title': title,
    }
    return HttpResponse(template.render(context, request))