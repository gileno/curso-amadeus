# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Início'),
        ),
    ]
