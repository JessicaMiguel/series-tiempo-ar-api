# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-09 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_catalog_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='error',
            field=models.TextField(default=b''),
        ),
    ]
