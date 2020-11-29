from tests.base import BaseTestCase

from elabodeal.models import Product


class TestProductModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Product, 'publisher'), True)
		self.assertEqual(hasattr(Product, 'category'), True)
		self.assertEqual(hasattr(Product, 'labels'), True)
		self.assertEqual(hasattr(Product, 'opinions'), True)
		self.assertEqual(hasattr(Product, 'title'), True)
		self.assertEqual(hasattr(Product, 'description'), True)
		self.assertEqual(hasattr(Product, 'price'), True)
		self.assertEqual(hasattr(Product, 'author'), True)
		self.assertEqual(hasattr(Product, 'page_count'), True)
		self.assertEqual(hasattr(Product, 'isbn'), True)
		self.assertEqual(hasattr(Product, 'contents'), True)
		self.assertEqual(hasattr(Product, 'age_category'), True)
		self.assertEqual(hasattr(Product, 'url_name'), True)
		self.assertEqual(hasattr(Product, 'average_rating'), True)
		self.assertEqual(hasattr(Product, 'rating_count'), True)
		self.assertEqual(hasattr(Product, 'cover_img'), True)
		self.assertEqual(hasattr(Product, 'pdf_file'), True)
		self.assertEqual(hasattr(Product, 'epub_file'), True)
		self.assertEqual(hasattr(Product, 'mobi_file'), True)
		self.assertEqual(hasattr(Product, 'published_at'), True)
		self.assertEqual(hasattr(Product, 'updated_at'), True)
