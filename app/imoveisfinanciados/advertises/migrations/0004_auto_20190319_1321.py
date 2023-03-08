# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-19 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertises', '0003_auto_20190307_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adcity',
            options={'get_latest_by': 'created', 'verbose_name': 'Municipal', 'verbose_name_plural': 'Municipais'},
        ),
        migrations.AlterModelOptions(
            name='adnational',
            options={'get_latest_by': 'created', 'verbose_name': 'Nacional', 'verbose_name_plural': 'Nacionais'},
        ),
        migrations.AlterModelOptions(
            name='adstate',
            options={'get_latest_by': 'created', 'verbose_name': 'Estadual', 'verbose_name_plural': 'Estaduais'},
        ),
    ]
