# coding=utf-8

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Resolution

class ResolutionList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    title = 'Resoluciones'
    model = Resolution

class ResolutionCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    title = 'Agregar nueva resolución'
    url = 'resolutions:list'
    success_url = reverse_lazy(url)
    model = Resolution
    fields = ['number', 'start_date', 'end_date', 'document', ]

class ResolutionEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    title = 'Editar Resolución'
    url = 'resolutions:list'
    success_url = reverse_lazy(url)
    model = Resolution
    fields = ['number', 'start_date', 'end_date', 'document']