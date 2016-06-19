import logging
from django.shortcuts import render
from django.views.generic import ListView
from . import models

logger = logging.getLogger('.'.join(['Iluminare2', __name__]))

# Create your views here.
class Listar(ListView):
    model = models.Pessoa