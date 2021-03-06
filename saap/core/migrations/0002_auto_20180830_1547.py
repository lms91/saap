# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-30 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areatrabalho',
            options={'ordering': ['descricao'], 'verbose_name': 'Área de trabalho', 'verbose_name_plural': 'Áreas de trabalho'},
        ),
        migrations.AlterModelOptions(
            name='impressoenderecamento',
            options={'verbose_name': 'Impresso para endereçamento', 'verbose_name_plural': 'Impressos para endereçamento'},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'ordering': ['nome'], 'verbose_name': 'Município', 'verbose_name_plural': 'Municípios'},
        ),
        migrations.AlterModelOptions(
            name='nivelinstrucao',
            options={'ordering': ['descricao'], 'verbose_name': 'Nível de instrução', 'verbose_name_plural': 'Níveis de instrução'},
        ),
        migrations.AlterModelOptions(
            name='operadorareatrabalho',
            options={'ordering': ['areatrabalho'], 'verbose_name': 'Operador', 'verbose_name_plural': 'Operadores'},
        ),
        migrations.AlterModelOptions(
            name='partido',
            options={'ordering': ['sigla'], 'verbose_name': 'Partido', 'verbose_name_plural': 'Partidos'},
        ),
        migrations.AlterModelOptions(
            name='regiaomunicipal',
            options={'verbose_name': 'Região municipal', 'verbose_name_plural': 'Regiões municipais'},
        ),
        migrations.AlterModelOptions(
            name='situacaomilitar',
            options={'verbose_name': 'Tipo de situação militar', 'verbose_name_plural': 'Tipos de situações militares'},
        ),
        migrations.AlterModelOptions(
            name='tipologradouro',
            options={'ordering': ('nome',), 'verbose_name': 'Tipo de logradouro', 'verbose_name_plural': 'Tipos de logradouros'},
        ),
        migrations.AlterModelOptions(
            name='trecho',
            options={'ordering': ['municipio__nome', 'regiao_municipal__nome', 'distrito__nome', 'bairro__nome', 'tipo__nome', 'logradouro__nome'], 'verbose_name': 'Trecho de logradouro', 'verbose_name_plural': 'Trechos de logradouro'},
        ),
        migrations.AlterField(
            model_name='bairro',
            name='codigo',
            field=models.PositiveIntegerField(default=0, help_text='Código do bairro no Cadastro Oficial do município', verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='bairro',
            name='outros_nomes',
            field=models.TextField(blank=True, help_text='Ocorrências similares', verbose_name='Outros nomes'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='nome',
            field=models.CharField(max_length=254, unique=True, verbose_name='Nome do distrito'),
        ),
        migrations.AlterField(
            model_name='filiacao',
            name='data',
            field=models.DateField(verbose_name='Data de filiação'),
        ),
        migrations.AlterField(
            model_name='filiacao',
            name='data_desfiliacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de desfiliação'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='altura_pagina',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Altura da página'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='alturaetiqueta',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Altura da etiquta'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='entre_colunas',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Distância entre colunas'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='entre_linhas',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Distância entre linhas'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='fontsize',
            field=models.DecimalField(decimal_places=2, help_text='Em pixels', max_digits=5, verbose_name='Tamanho da letra'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='largura_pagina',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Largura da página'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='larguraetiqueta',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Largura da etiqueta'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='margem_esquerda',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Margem esquerda'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='margem_superior',
            field=models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Margem superior'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='rotate',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Rotacionar rexto'),
        ),
        migrations.AlterField(
            model_name='impressoenderecamento',
            name='tipo',
            field=models.CharField(choices=[('ET', 'Folha de etiquetas'), ('EV', 'Envelopes')], default='ET', max_length=2, verbose_name='Tipo do impresso'),
        ),
        migrations.AlterField(
            model_name='nivelinstrucao',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Nível de instrução'),
        ),
        migrations.AlterField(
            model_name='operadorareatrabalho',
            name='areatrabalho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operadorareatrabalho_set', to='core.AreaTrabalho', verbose_name='Área de trabalho'),
        ),
        migrations.AlterField(
            model_name='operadorareatrabalho',
            name='grupos_associados',
            field=models.ManyToManyField(related_name='operadorareatrabalho_set', to='auth.Group', verbose_name='Grupos associados'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='endereco_residencia',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço residencial'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='fax_residencia',
            field=models.CharField(blank=True, max_length=50, verbose_name='Fax residencial'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='locais_atuacao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Locais de atuação'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='nivel_instrucao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.NivelInstrucao', verbose_name='Nível de instrução'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='nome_completo',
            field=models.CharField(max_length=50, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='nome_parlamentar',
            field=models.CharField(max_length=50, verbose_name='Nome do parlamentar'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='numero_gab_parlamentar',
            field=models.CharField(blank=True, max_length=10, verbose_name='Nº do gabinete'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='rg',
            field=models.CharField(blank=True, max_length=15, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='situacao_militar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SituacaoMilitar', verbose_name='Situação militar'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='telefone_residencia',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telefone residencial'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='titulo_eleitor',
            field=models.CharField(blank=True, max_length=15, verbose_name='Título de eleitor'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='data_criacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='data_extincao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de extinção'),
        ),
        migrations.AlterField(
            model_name='regiaomunicipal',
            name='nome',
            field=models.CharField(max_length=254, verbose_name='Região municipal'),
        ),
        migrations.AlterField(
            model_name='regiaomunicipal',
            name='tipo',
            field=models.CharField(choices=[('AU', 'Área urbana'), ('AR', 'Área rural'), ('UA', 'Área única')], default='AU', max_length=2, verbose_name='Tipo da região'),
        ),
        migrations.AlterField(
            model_name='situacaomilitar',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Situação militar'),
        ),
        migrations.AlterField(
            model_name='tipologradouro',
            name='nome',
            field=models.CharField(max_length=254, unique=True, verbose_name='Tipo de logradouro'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='cep',
            field=models.ManyToManyField(related_name='trechos_set', to='core.Cep', verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='lado',
            field=models.CharField(choices=[('NA', 'Não aplicável'), ('AL', 'Ambos os lados'), ('LE', 'Lado esquerdo'), ('LD', 'Lado direito')], default='AL', max_length=2, verbose_name='Lado do logradouro'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='numero_final',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número final'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='numero_inicial',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número inicial'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='regiao_municipal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.RegiaoMunicipal', verbose_name='Região municipal'),
        ),
        migrations.AlterField(
            model_name='trecho',
            name='tipo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.TipoLogradouro', verbose_name='Tipo de logradouro'),
        ),
    ]
