import uuid
from tests import BaseTestCase
from elabodeal.models import ProductPremiere


class ProductPremiereModelTest(BaseTestCase):

	def test_fields(self):
		self.assertEqual(hasattr(ProductPremiere, 'id'), True)
		self.assertEqual(
			ProductPremiere._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			ProductPremiere._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			ProductPremiere._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(ProductPremiere, 'datetime'), True)

		self.assertEqual(hasattr(ProductPremiere, 'created_at'), True)
		self.assertEqual(
			ProductPremiere._meta.get_field('created_at').auto_now_add,
			True
		)

		self.assertEqual(hasattr(ProductPremiere, 'updated_at'), True)
		self.assertEqual(
			ProductPremiere._meta.get_field('updated_at').auto_now,
			True
		)