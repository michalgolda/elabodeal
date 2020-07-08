from tests.base import BaseTestCase

from elabodeal.models import Category


class TestCategoryModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Category, 'name'), True)