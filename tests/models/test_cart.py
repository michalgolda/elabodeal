from tests.base import BaseTestCase

from elabodeal.models import Cart


class TestCartModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Cart, 'title'), True)
		self.assertEqual(hasattr(Cart, 'description'), True)
		self.assertEqual(hasattr(Cart, 'user'), True)
