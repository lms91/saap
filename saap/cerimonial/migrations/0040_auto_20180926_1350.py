# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-26 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0039_auto_20180926_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(blank=True, default=0, max_length=5, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='numero',
            field=models.CharField(blank=True, default=0, max_length=5, verbose_name='Número'),
        ),
    ]
