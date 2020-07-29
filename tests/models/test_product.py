from tests.base import BaseTestCase

from elabodeal.models import Product


class TestProductModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Product, 'category'), True)
		self.assertEqual(hasattr(Product, 'author'), True)
		self.assertEqual(hasattr(Product, 'user'), True)
		self.assertEqual(hasattr(Product, 'title'), True)
		self.assertEqual(hasattr(Product, 'description'), True)
		self.assertEqual(hasattr(Product, 'price'), True)
		self.assertEqual(hasattr(Product, 'page_count'), True)
		self.assertEqual(hasattr(Product, 'isbn'), True)
		self.assertEqual(hasattr(Product, 'cover_img'), True)
		self.assertEqual(hasattr(Product, 'pdf'), True)
		self.assertEqual(hasattr(Product, 'epub'), True)
		self.assertEqual(hasattr(Product, 'mobi'), True)
		self.assertEqual(hasattr(Product, 'created_at'), True)
		self.assertEqual(hasattr(Product, 'updated_at'), True)
		self.assertEqual(hasattr(Product, 'age_categories'), True)
		self.assertEqual(hasattr(Product, 'url_name'), True)
		self.assertEqual(hasattr(Product, 'count_views'), True)
		self.assertEqual(hasattr(Product, 'contents'), True)
