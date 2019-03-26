import json

from django_datajsonar.models import Node
from mock import Mock, patch
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from nose.tools import raises

from series_tiempo_ar_api.libs.datajsonar_repositories.distribution_repository import DistributionRepository
from series_tiempo_ar_api.libs.indexing import constants


class DistributionRepositoryTests(TestCase):

    def test_get_time_index(self):
        time_index_field = Mock(metadata=json.dumps({constants.SPECIAL_TYPE: constants.TIME_INDEX}))
        distribution = Mock()
        distribution.field_set.all.return_value = [time_index_field]

        self.assertEqual(DistributionRepository(distribution).get_time_index_series(), time_index_field)

    @raises(ObjectDoesNotExist)
    def test_get_time_index_none_exists(self):
        distribution = Mock()
        distribution.field_set.all.return_value = []
        DistributionRepository(distribution).get_time_index_series()

    def test_get_node(self):
        distribution = Mock()
        distribution.dataset.catalog.identifier = 'test_node'

        node = Node(catalog_id='test_node')
        with patch('series_tiempo_ar_api.libs.datajsonar_repositories.distribution_repository.Node') as fake_node:
            fake_node.objects.get.return_value = node
            self.assertTrue(fake_node.objects.get.called_with(catalog_id='test_node'))
            self.assertEqual(DistributionRepository(distribution).get_node(), node)

    @patch('series_tiempo_ar_api.libs.datajsonar_repositories.distribution_repository.Node')
    @patch('series_tiempo_ar_api.libs.datajsonar_repositories.node_repository.NodeRepository')
    def test_get_data_json(self, repository, fake_node):
        distribution = Mock()
        node = Node(catalog_id='test_node')
        fake_node.objects.get.return_value = node
        DistributionRepository(distribution).get_data_json()
        self.assertTrue(repository.called_with(node))
