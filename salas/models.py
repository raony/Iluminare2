from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
