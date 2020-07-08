from tests.base import BaseTestCase

from elabodeal.models import VerifyCode


class TestVerfiyCodeModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(VerifyCode, 'email'), True)
		self.assertEqual(hasattr(VerifyCode, 'code'), True)
		self.assertEqual(hasattr(VerifyCode, 'created_at'), True)
