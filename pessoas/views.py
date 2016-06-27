import logging
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models

logger = logging.getLogger('.'.join(['Iluminare2', __name__]))

# Create your views here.
class Listar(ListView):
    model = models.Pessoa

class Adicionar(CreateView):
    model = models.Pessoa
    fields = '__all__'
    success_url = reverse_lazy('pessoas-listar')
    template_name = 'pessoas/pessoa_adicionar.html'

class Visualizar(DetailView):
    model = models.Pessoa

class Atualizar(UpdateView):
    model = models.Pessoa
    fields = '__all__'
    template_name = 'pessoas/pessoa_atualizar.html'

    def get_success_url(self):
        return reverse_lazy('pessoas-visualizar', args=[self.object.pk,])