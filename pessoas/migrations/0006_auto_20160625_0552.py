# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0005_auto_20160625_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pais',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True, verbose_name='gênero'),
        ),
    ]
