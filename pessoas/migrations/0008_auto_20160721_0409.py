# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 04:09
from __future__ import unicode_literals

from django.db import migrations, models

from unidecode import unidecode

def combinar_nomes(apps, schema_editor):
    Pessoa = apps.get_model("pessoas", "Pessoa")
    for pessoa in Pessoa.objects.all():
        pessoa.nome_completo = unidecode(" ".join([pessoa.nome, pessoa.sobrenome]).lower())
        pessoa.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('pessoas', '0007_pessoa_nome_completo'),
    ]

    operations = [
        migrations.RunPython(combinar_nomes),
    ]