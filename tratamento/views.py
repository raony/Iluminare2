from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.

class ListarTratamento(ListView):
    pass

class VisualizarTratamento(DetailView):
    pass

class AdicionarTratamento(CreateView):
    pass

class AtualizarTratamento(UpdateView):
    pass
