from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin
from django import forms
from datetime import datetime

from pessoas.models import Pessoa
from .models import Atendimento

# Create your views here.
class Entrada(ListView):
    template_name = 'atendimentos/atendimentos_entrada.html'

    def get_context_data(self, **kwargs):
        context = super(Entrada, self).get_context_data(**kwargs)
        if 'q' in self.request.GET:
            context['q'] = self.request.GET['q']
        return context

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Pessoa.objects.filter_by_name(self.request.GET['q'])
        return []

class Visualizar(ListView):
    def get_queryset(self):
        if 'pk' in self.kwargs:
            paciente = get_object_or_404(Pessoa, pk=self.kwargs['pk'])

            return Atendimento.objects.filter(paciente = paciente, hora__date=datetime.now().date())