# coding=utf-8

from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader
from .models import Career

# Create your views here.

def viewCareers(request):
    title = 'Carreras Acreditadas'
    careers = Career.objects.all()
    template = loader.get_template('view_careers.html')
    context = {
        'careers': careers,
        'title':  title,
    }
    return HttpResponse(template.render(context, request))