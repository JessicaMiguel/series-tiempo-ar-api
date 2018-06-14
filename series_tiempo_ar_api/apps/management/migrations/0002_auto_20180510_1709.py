# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-10 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from django_datajsonar.models import Node
from series_tiempo_ar_api.apps.management import models as mgmt_models


def migrate_nodes(*_):
    nodes = mgmt_models.Node.objects.all()

    for node in nodes:
        Node(catalog_id=node.catalog_id,
             catalog_url=node.catalog_url,
             indexable=node.indexable).save()


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_auto_20180507_1500'),
        ('django_datajsonar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readdatajsontask',
            name='catalogs',
        ),
        migrations.RunPython(migrate_nodes),
        migrations.AddField(
            model_name='indicator',
            name='node_tmp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node', null=True),
        ),
    ]
