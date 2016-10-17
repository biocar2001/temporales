# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_auto_20161016_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='ofertas',
        ),
        migrations.AddField(
            model_name='oferta',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Empresa'),
        ),
        migrations.RemoveField(
            model_name='persona',
            name='empresa',
        ),
        migrations.AddField(
            model_name='persona',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Empresa'),
        ),
    ]
