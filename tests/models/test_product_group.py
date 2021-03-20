import uuid
from tests import BaseTestCase

from elabodeal.models import ProductGroup


class ProductGroupModelTest(BaseTestCase):

	def test_fields(self):
		self.assertEqual(hasattr(ProductGroup, 'id'), True)
		self.assertEqual(
			ProductGroup._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			ProductGroup._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			ProductGroup._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(ProductGroup, 'publisher'), True)

		self.assertEqual(hasattr(ProductGroup, 'name'), True)
		self.assertEqual(
			ProductGroup._meta.get_field('name').max_length,
			ProductGroup.MAX_NAME_LENGTH
		)

		self.assertEqual(hasattr(ProductGroup, 'created_at'), True)
		self.assertEqual(
			ProductGroup._meta.get_field('created_at').auto_now_add,
			True
		)

		self.assertEqual(hasattr(ProductGroup, 'updated_at'), True)
		self.assertEqual(
			ProductGroup._meta.get_field('updated_at').auto_now,
			True
		)