# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Career
from django.core.paginator import Paginator, InvalidPage, EmptyPage

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

def viewCareers(request):
    title = 'Carreras Acreditadas Modelo Nacional'
    template = loader.get_template('view_careers.html')
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
    }
    return HttpResponse(template.render(context, request))