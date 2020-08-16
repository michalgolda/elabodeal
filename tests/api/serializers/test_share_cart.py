from tests.base import BaseTestCase

from elabodeal.api.serializers import ShareCartSerializer


class TestShareCartSerializer(BaseTestCase):
	def test_simple(self):
		serializer = ShareCartSerializer(data={
				'title': 'test',
				'description': 'test'
			})

		serializer.is_valid()

		self.assertEqual(serializer.data['title'], 'test')
		self.assertEqual(serializer.data['description'], 'test')