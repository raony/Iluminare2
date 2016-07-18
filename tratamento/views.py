from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tratamento, Sessao
from pessoas.models import Pessoa

from datetime import datetime
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

    def get_initial(self):
        result = super(AdicionarTratamento, self).get_initial()
        if 'pessoapk' in self.kwargs:
            try:
                result.update({'paciente': Pessoa.objects.get(pk=self.kwargs['pessoapk'])})
            except Pessoa.DoesNotExist:
                pass
        return result

class AtualizarTratamento(UpdateView):
    model = Tratamento
    fields = '__all__'
    template_name = 'tratamento/tratamento_atualizar.html'

    def get_success_url(self):
        return reverse_lazy('tratamentos-visualizar', args=[self.object.pk, ])

class AdicionarSessao(CreateView):
    model = Sessao
    fields = '__all__'
    template_name = 'tratamento/sessao_adicionar.html'

    def get_success_url(self):
        return reverse_lazy('tratamentos-visualizar', args=[self.kwargs['tratamentopk']])

    def get_initial(self):
        result = super(AdicionarSessao, self).get_initial()
        result.update({'tratamento': get_object_or_404(Tratamento, pk=self.kwargs['tratamentopk'])})
        return result

class RemoverSessao(DeleteView):
    model = Sessao

    def get_success_url(self):
        return reverse_lazy('tratamentos-visualizar', args=[self.kwargs['tratamentopk']])