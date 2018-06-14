#!coding=utf8
from __future__ import unicode_literals

from django.db import migrations
import django_datajsonar.models
import series_tiempo_ar_api.apps.api.models as api_models


def move(*_):
    for catalog in api_models.Catalog.objects.all():
        django_datajsonar.models.Catalog.objects.get_or_create(
            title=catalog.title,
            identifier=catalog.identifier,
            metadata=catalog.metadata,
        )

    for dataset in api_models.Dataset.objects.all():
        django_datajsonar.models.Dataset.objects.get_or_create(
            title="",
            identifier=dataset.identifier,
            catalog=django_datajsonar.models.Catalog.objects.get(identifier=dataset.catalog.identifier),
            metadata=dataset.metadata,
            indexable=dataset.indexable,
        )

    for distribution in api_models.Distribution.objects.all():
        dataset = django_datajsonar.models.Dataset.objects.get(
            identifier=distribution.dataset.identifier,
            catalog__identifier=distribution.dataset.catalog.identifier
        )
        django_datajsonar.models.Distribution.objects.get_or_create(
            identifier=distribution.identifier,
            metadata=distribution.metadata,
            dataset=dataset,
            download_url=distribution.download_url,
            data_hash=distribution.data_hash,
            data_file=distribution.data_file
        )

    for field in api_models.Field.objects.iterator():
        django_datajsonar.models.Field(
            title=field.title,
            identifier=field.series_id,
            metadata=field.metadata,
            distribution=django_datajsonar.models.Distribution.objects.get(
                identifier=field.distribution.identifier,
                dataset__catalog__identifier=field.distribution.dataset.catalog.identifier
            )
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('management', 'rename_node_tmp'),
        ('api', '0034_distribution_error'),
        ('django_datajsonar', '0002_auto_20180507_1752'),
    ]

    operations = [
        migrations.RunPython(move)
    ]
