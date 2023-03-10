# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Título')),
                ('image', models.ImageField(upload_to='realties/', verbose_name='Foto')),
            ],
            options={
                'verbose_name_plural': 'Fotos',
                'verbose_name': 'Foto',
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título do anúncio')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('type', models.CharField(choices=[('apt', 'Apartamento'), ('casa', 'Casa'), ('cond', 'Condomínio')], max_length=4, verbose_name='Tipo do imóvel')),
                ('value', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço')),
                ('bedroom', models.IntegerField(verbose_name='Quartos')),
                ('bathroom', models.IntegerField(verbose_name='Banheiros')),
                ('size', models.IntegerField(verbose_name='Metros quadrados')),
                ('main_image', models.ImageField(upload_to='realties/', verbose_name='Foto principal')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='Cidade')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Imóveis',
                'ordering': ['value', '-modified', '-created'],
                'verbose_name': 'Imóvel',
                'db_table': 'realty',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='realty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='realty.Realty', verbose_name='Imóvel'),
        ),
    ]
