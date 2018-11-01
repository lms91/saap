# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-18 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180918_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50)),
                ('sigla', models.CharField(max_length=2)),
                ('regiao', models.CharField(choices=[('CO', 'Centro-Oeste'), ('NE', 'Nordeste'), ('NO', 'Norte'), ('SE', 'Sudeste'), ('SL', 'Sul'), ('EX', 'Exterior')], max_length=2, verbose_name='Região geográfica')),
            ],
            options={
                'verbose_name': 'Estado',
                'ordering': ['nome'],
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='regiao',
        ),
        migrations.AlterField(
            model_name='municipio',
            name='uf',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins'), ('EX', 'Exterior')], max_length=2, verbose_name='UF'),
        ),
    ]