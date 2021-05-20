import uuid
from tests.base import BaseTestCase

from elabodeal.models import Category


class TestCategoryModel(BaseTestCase):
	
	def test_fields(self):
		self.assertEqual(hasattr(Category, 'id'), True)
		self.assertEqual(
			Category._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			Category._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			Category._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(Category, 'name'), True)
		self.assertEqual(
			Category._meta.get_field('name').max_length,
			Category.MAX_NAME_LENGTH
		)

	def test_options(self):
		self.assertEqual(
			Category._meta.verbose_name_plural, 
			'Categories'
		)

	def test_whether_str_method_return_name(self):
		category = Category(name='Test')

		self.assertEqual(str(category), 'Test')