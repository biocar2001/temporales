# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-16 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_auto_20161012_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='prize_healthcare',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='prize_home',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
