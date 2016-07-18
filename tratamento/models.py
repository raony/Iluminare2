from django.db import models

from pessoas.models import Pessoa
from salas.models import Sala

# Create your models here.
class Tratamento(models.Model):
    paciente = models.ForeignKey(Pessoa)
    inicio = models.DateField()
    ativo = models.BooleanField(default=True)

class Sessao(models.Model):
    tratamento = models.ForeignKey(Tratamento)
    sala = models.ForeignKey(Sala)
    quantidade = models.PositiveSmallIntegerField()

def sessao_create(self, *args, **kwargs):
    sessao = Sessao(*args, **kwargs)
    sessao.save()
    return sessao