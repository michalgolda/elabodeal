from tests.base import BaseTestCase

from elabodeal.models import SharedCartItem


class TestSharedCartItemModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(SharedCartItem, 'shared_cart'), True)
		self.assertEqual(hasattr(SharedCartItem, 'product'), True)
