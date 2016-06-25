import logging
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models

logger = logging.getLogger('.'.join(['Iluminare2', __name__]))

# Create your views here.
class Listar(ListView):
    model = models.Pessoa

class Adicionar(CreateView):
    model = models.Pessoa
    fields = '__all__'
    success_url = reverse_lazy('pessoas-listar')

class Visualizar(DetailView):
    model = models.Pessoa