# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0015_auto_20161019_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='observaciones_time_contrato',
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(default='no phone', max_length=20, verbose_name='apellidos'),
        ),
    ]
