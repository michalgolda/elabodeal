from tests.base import BaseTestCase

from elabodeal.models import CartItem


class TestCartItemModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(CartItem, 'cart'), True)
		self.assertEqual(hasattr(CartItem, 'product'), True)