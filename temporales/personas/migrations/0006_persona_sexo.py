# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_auto_20160923_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.IntegerField(default=1, verbose_name='sexo'),
            preserve_default=False,
        ),
    ]
