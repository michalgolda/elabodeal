from tests.base import BaseTestCase

from elabodeal.models import Product


class TestProductModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Product, 'category'), True)
		self.assertEqual(hasattr(Product, 'author'), True)
		self.assertEqual(hasattr(Product, 'title'), True)
		self.assertEqual(hasattr(Product, 'description'), True)
		self.assertEqual(hasattr(Product, 'price'), True)
		self.assertEqual(hasattr(Product, 'cover_img_url'), True)
		self.assertEqual(hasattr(Product, 'created_at'), True)
		self.assertEqual(hasattr(Product, 'updated_at'), True)
