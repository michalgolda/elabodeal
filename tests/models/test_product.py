import uuid
from tests.base import BaseTestCase

from elabodeal.models import Product


class ProductModelTest(BaseTestCase):
	
	def test_fields(self):
		self.assertEqual(hasattr(Product, 'id'), True)
		self.assertEqual(
			Product._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			Product._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			Product._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(Product, 'publisher'), True)
		self.assertEqual(hasattr(Product, 'group'), True)
		self.assertEqual(hasattr(Product, 'category'), True)

		self.assertEqual(hasattr(Product, 'title'), True)
		self.assertEqual(
			Product._meta.get_field('title').max_length,
			Product.MAX_TITLE_LENGTH
		)

		self.assertEqual(hasattr(Product, 'description'), True)
		self.assertEqual(
			Product._meta.get_field('description').max_length,
			Product.MAX_DESCRIPTION_LENGTH
		)

		self.assertEqual(hasattr(Product, 'contents'), True)
		self.assertEqual(
			Product._meta.get_field('contents').max_length,
			Product.MAX_CONTENTS_LENGTH
		)
		self.assertEqual(
			Product._meta.get_field('contents').null,
			True
		)
		self.assertEqual(
			Product._meta.get_field('contents').blank,
			True
		)

		self.assertEqual(hasattr(Product, 'author'), True)
		self.assertEqual(
			Product._meta.get_field('author'). max_length,
			Product.MAX_AUTHOR_LENGTH
		)

		self.assertEqual(hasattr(Product, 'isbn'), True)
		self.assertEqual(
			Product._meta.get_field('isbn').max_length,
			Product.MAX_ISBN_LENGTH
		)

		self.assertEqual(hasattr(Product, 'price'), True)
		self.assertEqual(
			Product._meta.get_field('price').max_digits,
			Product.MAX_PRICE_DIGITS
		)
		self.assertEqual(
			Product._meta.get_field('price').decimal_places,
			Product.PRICE_DECIMALS_PLACES
		)
		
		self.assertEqual(hasattr(Product, 'copies'), True)
		self.assertEqual(
			Product._meta.get_field('copies').default,
			0
		)

		self.assertEqual(hasattr(Product, 'page_count'), True)

		self.assertEqual(hasattr(Product, 'cover_img'), True)
		self.assertEqual(hasattr(Product, 'other_images'), True)
		self.assertEqual(hasattr(Product, 'files'), True)

		self.assertEqual(hasattr(Product, 'age_category'), True)
		self.assertEqual(
			Product._meta.get_field('age_category').choices,
			Product.AgeCategory.choices
		)

		self.assertEqual(hasattr(Product, 'average_rating'), True)
		self.assertEqual(
			Product._meta.get_field('average_rating').default,
			0
		)

		self.assertEqual(hasattr(Product, 'rating_count'), True)
		self.assertEqual(
			Product._meta.get_field('rating_count').default,
			0
		)

		self.assertEqual(hasattr(Product, 'premiere'), True)
		self.assertEqual(
			Product._meta.get_field('premiere').null,
			True
		)

		self.assertEqual(hasattr(Product, 'created_at'), True)
		self.assertEqual(
			Product._meta.get_field('created_at').auto_now_add,
			True
		)

		self.assertEqual(hasattr(Product, 'updated_at'), True)
		self.assertEqual(
			Product._meta.get_field('updated_at').auto_now,
			True
		)

	def test_filled_stars_property(self):
		product = Product()
		product.average_rating = 4.0

		self.assertEqual(product.filled_stars, range(4))

	def test_empty_stars_property(self):
		product = Product()
		product.average_rating = 4.0

		self.assertEqual(product.empty_stars, range(1))
