# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-08 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20190123_1534'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskCron',
        ),
        migrations.RemoveField(
            model_name='integrationtestconfig',
            name='time',
        ),
    ]
