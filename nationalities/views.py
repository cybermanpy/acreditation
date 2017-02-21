# coding=utf-8

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Nationality
from namecareers.forms import FormSearch
from django.core.paginator import Paginator, InvalidPage, EmptyPage


@login_required(login_url='/login/')
def viewNationality(request):
    title = 'Descripcion de la nacionalidad'
    template = loader.get_template('view_nationality.html')
    request.session['s_text'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            request.session['s_text'] = search
            listNationality = Nationality.objects.filter(origin__icontains=search)
            context = {
                'title': title,
                'listNationality': listNationality,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listPaginator = Nationality.objects.all()
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listNationality = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listNationality = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listNationality': listNationality,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


class NationalityCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    title = 'Agregar nueva nacionalidad'
    url = 'nationalities:view'
    success_url = reverse_lazy(url)
    model = Nationality
    fields = ['origin',]

class NationalityEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    title = 'Editar nacionalidad'
    url = 'nationalities:view'
    success_url = reverse_lazy(url)
    model = Nationality
    fields = ['origin',]
