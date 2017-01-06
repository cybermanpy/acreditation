# coding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NameCareer
from .forms import NameCareerForm, FormSearch
from django.core.paginator import Paginator, InvalidPage, EmptyPage

@login_required(login_url='/login/')
def viewNameCareer(request):
    title = 'Nombre de Carreras'
    template = loader.get_template('view_namecareer.html')
    request.session['s_text'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            request.session['s_text'] = search
            listNameCareer = NameCareer.objects.filter(description__icontains=search)
            context = {
                'title': title,
                'listNameCareer': listNameCareer,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listPaginator = NameCareer.objects.all()
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listNameCareer = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listNameCareer = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listNameCareer': listNameCareer,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def newNameCareer(request):
    title = 'Agregar nueva carrera'
    template = loader.get_template('new_namecareer.html')
    if request.method == 'POST':
        form = NameCareerForm(request.POST)
        if form.is_valid():
            form.save()
            url = 'namecareers:list'
            return HttpResponseRedirect(reverse(url))
    else:
        form = NameCareerForm()
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def editNameCareer(request, pk):
    title = 'Editar nombre de carrera'
    template = loader.get_template('new_namecareer.html')
    ins = get_object_or_404(NameCareer, pk=pk)
    if request.method == 'POST':
        form = NameCareerForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            url = 'namecareers:list'
            return HttpResponseRedirect(reverse(url))
    else:
        form = NameCareerForm(instance=ins)
    context = {
        'title': title,
        'form': form,
    }
    return HttpResponse(template.render(context, request))