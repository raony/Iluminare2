from django.db import models

from pessoas.models import Pessoa
from salas.models import Sala

# Create your models here.
class Tratamento(models.Model):
    paciente = models.ForeignKey(Pessoa)
    inicio = models.DateField()
    ativo = models.BooleanField(default=True)

class Sessoes(models.Model):
    tratamento = models.ForeignKey(Tratamento)
    sala = models.ForeignKey(Sala)
    quantidade = models.PositiveSmallIntegerField(default=0)

class Atendimento(models.Model):
    EVENTOS = (
        ('chegada', 'chegada'),
        ('encaminhado à sala', 'encaminhado à sala'),
        ('em atendimento', 'em atendimento'),
        ('atendimento finalizado', 'atendimento finalizado'),
    )

    hora = models.DateTimeField()
    paciente = models.ForeignKey(Pessoa)
    evento = models.CharField(max_length=200, choices=EVENTOS)