# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0014_auto_20161018_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='observaciones_prize_healthcare',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='observaciones_prize_home',
        ),
    ]