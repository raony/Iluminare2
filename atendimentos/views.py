from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Entrada(TemplateView):
    template_name = 'atendimentos/atendimentos_entrada.html'