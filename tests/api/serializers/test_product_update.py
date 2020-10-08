from tests.base import BaseTestCase
from elabodeal.api.serializers import ProductUpdateSerializer


class TestProductUpdateSerializer(BaseTestCase):
	def test_simple(self):
		data = {
			'title': 'test',
			'author': 'test'
		}
		serializer = ProductUpdateSerializer(data=data)

		self.assertEqual(serializer.is_valid(), True)
		self.assertEquals(serializer.data, data)