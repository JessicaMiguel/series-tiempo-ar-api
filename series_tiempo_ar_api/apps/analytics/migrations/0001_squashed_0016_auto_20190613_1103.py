# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('analytics', '0001_initial'), ('analytics', '0002_node'), ('analytics', '0003_delete_node'), ('analytics', '0004_auto_20180117_1045'), ('analytics', '0005_importconfig'), ('analytics', '0006_analyticsimporttask'), ('analytics', '0007_query_api_mgmt_id'), ('analytics', '0008_auto_20180725_1114_squashed_0009_query_uri'), ('analytics', '0009_importconfig_last_cursor'), ('analytics', '0010_importconfig_time'), ('analytics', '0011_auto_20190123_1530'), ('analytics', '0012_auto_20190124_1117'), ('analytics', '0013_remove_importconfig_time'), ('analytics', '0014_auto_20190220_1127'), ('analytics', '0015_analyticsimporttask_node'), ('analytics', '0016_auto_20190613_1103')]

    initial = True

    dependencies = [
        ('django_datajsonar', '0006_synchronizer_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.TextField()),
                ('args', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=200, null=True)),
                ('params', models.TextField()),
                ('api_mgmt_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('request_time', models.DecimalField(decimal_places=25, default=0, max_digits=30)),
                ('status_code', models.IntegerField(default=0)),
                ('user_agent', models.TextField(default='')),
                ('uri', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'Tabla consultas',
            },
        ),
        migrations.CreateModel(
            name='ImportConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.URLField()),
                ('token', models.CharField(max_length=64)),
                ('kong_api_id', models.CharField(max_length=64)),
                ('last_cursor', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Configuración de importación de analytics',
            },
        ),
        migrations.CreateModel(
            name='AnalyticsImportTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RUNNING', 'Procesando catálogos'), ('FINISHED', 'Finalizada')], max_length=20)),
                ('logs', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(null=True)),
                ('node', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node')),
            ],
            options={
                'verbose_name': 'Corrida de importación de analytics',
                'verbose_name_plural': 'Corridas de importación de analytics',
            },
        ),
        migrations.CreateModel(
            name='HitsIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_id', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('hits', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Consultas por día de serie',
                'verbose_name_plural': 'Consultas por día de series',
            },
        ),
        migrations.AlterUniqueTogether(
            name='hitsindicator',
            unique_together=set([('serie_id', 'date')]),
        ),
    ]