from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tratamento
# Create your views here.

class ListarTratamento(ListView):
    model = Tratamento

class VisualizarTratamento(DetailView):
    model = Tratamento

class AdicionarTratamento(CreateView):
    model = Tratamento
    fields = '__all__'
    success_url = reverse_lazy('tratamentos-listar')
    template_name = 'tratamento/tratamento_adicionar.html'

class AtualizarTratamento(UpdateView):
    model = Tratamento
    fields = '__all__'
    template_name = 'tratamento/tratamento_atualizar.html'

    def get_success_url(self):
        return reverse_lazy('tratamentos-visualizar', args=[self.object.pk, ])
