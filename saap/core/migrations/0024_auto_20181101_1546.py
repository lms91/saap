# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-01 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20181101_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrito',
            name='nome',
            field=models.CharField(max_length=254, verbose_name='Nome do distrito'),
        ),
    ]