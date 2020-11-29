from tests.base import BaseTestCase

from elabodeal.models import SharedCart


class TestSharedCartModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(SharedCart, 'uuid'), True)
		self.assertEqual(hasattr(SharedCart, 'cart'), True)
		self.assertEqual(hasattr(SharedCart, 'shared_at'), True)
