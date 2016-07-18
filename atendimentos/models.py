from django.db import models
from django.utils import timezone
from pessoas.models import Pessoa
from tratamento.models import Tratamento


# Create your models here.
class Atendimento(models.Model):
    EVENTOS = (
        ('chegada', 'chegada'),
        ('encaminhado à sala', 'encaminhado à sala'),
        ('em atendimento', 'em atendimento'),
        ('atendimento finalizado', 'atendimento finalizado'),
    )

    hora = models.DateTimeField(default=timezone.now)
    paciente = models.ForeignKey(Pessoa)
    evento = models.CharField(max_length=200, choices=EVENTOS)