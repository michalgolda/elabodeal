from tests.base import BaseTestCase

from elabodeal.models import PurchasedProduct


class TestPurchasedProductModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(PurchasedProduct, 'product'), True)
		self.assertEqual(hasattr(PurchasedProduct, 'user'), True)