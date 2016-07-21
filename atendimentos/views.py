from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django import forms

from pessoas.models import Pessoa

# Create your views here.
class Entrada(ListView):
    template_name = 'atendimentos/atendimentos_entrada.html'

    def get_context_data(self, **kwargs):
        context = super(Entrada, self).get_context_data(**kwargs)
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']
        return context

    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        if 'q' in self.request.GET:
            return Pessoa.objects.filter_by_name(self.request.GET['q'])
        return []