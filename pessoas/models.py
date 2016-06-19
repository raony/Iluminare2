from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200, blank=False, default=None)
    sobrenome = models.CharField(max_length=200, blank=False, default=None)