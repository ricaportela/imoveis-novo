# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 15:48
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations
from imoveisfinanciados.utils.slug import unique_slugify


def update_slugs(apps, schema_editor):
    CityModel = apps.get_model("core", "City")

    for instance in CityModel.objects.all():
        instance.slug = unique_slugify(instance, instance.name)
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_city_slug'),
    ]

    operations = [
        migrations.RunPython(update_slugs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]