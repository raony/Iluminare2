from django.db import models
from django.utils import timezone
from pessoas.models import Pessoa
from tratamento.models import Tratamento


# Create your models here.
class Atendimento(models.Model):
    EVENTOS = (
        ('chegada', 'Chegada'),
        ('encaminhado à sala', 'Encaminhado à sala'),
        ('em atendimento', 'Em atendimento'),
        ('atendimento finalizado', 'Atendimento finalizado'),
    )

    hora = models.DateTimeField(default=timezone.now)
    paciente = models.ForeignKey(Pessoa)
    evento = models.CharField(max_length=200, choices=EVENTOS)
    _mensagem = models.TextField()