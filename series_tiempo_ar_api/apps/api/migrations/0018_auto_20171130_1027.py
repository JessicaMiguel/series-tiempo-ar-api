# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_query_params'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='ip_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
