import logging
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models

logger = logging.getLogger('.'.join(['Iluminare2', __name__]))

# Create your views here.
class ListarSala(ListView):
    model = models.Sala

class AdicionarSala(CreateView):
    model = models.Sala
    fields = '__all__'
    success_url = reverse_lazy('salas-listar')
    template_name = 'salas/sala_adicionar.html'

class VisualizarSala(DetailView):
    model = models.Sala

class AtualizarSala(UpdateView):
    model = models.Sala
    fields = '__all__'
    template_name = 'salas/sala_atualizar.html'

    def get_success_url(self):
        return reverse_lazy('salas-visualizar', args=[self.object.pk,])