from tests.base import BaseTestCase

from elabodeal.models import AgeCategory


class TestAgeCategoryModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(AgeCategory, 'value'), True)
