# coding=utf-8

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Resolution
from namecareers.forms import FormSearch
from django.core.paginator import Paginator, InvalidPage, EmptyPage



@login_required(login_url='/login/')
def viewResolution(request):
    title = 'Nombre de Carreras'
    template = loader.get_template('view_resolution.html')
    request.session['s_text'] = ''
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            search = request.POST['text']
            request.session['s_text'] = search
            listResolution = Resolution.objects.filter(number=search)
            context = {
                'title': title,
                'listResolution': listResolution,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = FormSearch()
    listPaginator = Resolution.objects.all()
    paginator = Paginator(listPaginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        listResolution = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listResolution = paginator.page(paginator.num_pages)
    context = {
        'title': title,
        'listResolution': listResolution,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


class ResolutionList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    title = 'Resoluciones'
    model = Resolution
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ResolutionList, self).get_context_data(**kwargs) 
        listResolution = Resolution.objects.all()
        paginator = Paginator(listResolution, self.paginate_by)
        try:
            page = int(self.request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            object_list = paginator.page(page)
        except (EmptyPage, InvalidPage):
            object_list = paginator.page(paginator.num_pages)
        context['object_list'] = object_list
        return context

class ResolutionCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    title = 'Agregar nueva resolución'
    url = 'resolutions:view'
    success_url = reverse_lazy(url)
    model = Resolution
    fields = ['number', 'start_date', 'end_date', 'document', ]

class ResolutionEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    title = 'Editar Resolución'
    url = 'resolutions:view'
    success_url = reverse_lazy(url)
    model = Resolution
    fields = ['number', 'start_date', 'end_date', 'document']
