from tests.base import BaseTestCase

from elabodeal.models import SharedCart


class TestSharedCartModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(SharedCart, 'title'), True)
		self.assertEqual(hasattr(SharedCart, 'description'), True)
		self.assertEqual(hasattr(SharedCart, 'created_at'), True)

	def test_generate_code_function(self):
		code = SharedCart.generate_code()
		self.assertEqual(len(code), 10)

	def test_generate_code_function_using_another_parameters(self):
		code = SharedCart.generate_code(5)
		self.assertEqual(len(code), 5)