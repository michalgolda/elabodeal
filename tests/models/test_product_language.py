import uuid
from tests import BaseTestCase

from elabodeal.models import ProductLanguage


class ProductLanguageModelTest(BaseTestCase):

	def test_fields(self):
		self.assertEqual(hasattr(ProductLanguage, 'id'), True)
		self.assertEqual(
			ProductLanguage._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			ProductLanguage._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			ProductLanguage._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(ProductLanguage, 'code'), True)
		self.assertEqual(
			ProductLanguage._meta.get_field('code').max_length,
			ProductLanguage.MAX_CODE_LENGTH
		)

		self.assertEqual(hasattr(ProductLanguage, 'name'), True)
		self.assertEqual(
			ProductLanguage._meta.get_field('name').max_length,
			ProductLanguage.MAX_NAME_LENGTH
		)
