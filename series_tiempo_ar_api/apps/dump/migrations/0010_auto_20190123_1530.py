# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-23 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dump', '0009_auto_20181219_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generatedumptask',
            options={'verbose_name': 'Corrida de generación de dumps', 'verbose_name_plural': 'Corridas de generación de dumps'},
        ),
    ]
