import uuid

from tests.base import TestCase
from elabodeal.models import VerificationCode


class TestVerificationCodeModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(VerificationCode, 'id'), True)
		self.assertEqual(hasattr(VerificationCode, 'code'), True)
		self.assertEqual(hasattr(VerificationCode, 'email'), True)
		self.assertEqual(hasattr(VerificationCode, 'created_at'), True)
		self.assertEqual(hasattr(VerificationCode, 'expiration_at'), True)

		id_field = VerificationCode._meta.get_field('id')
		code_field = VerificationCode._meta.get_field('code')
		created_at_field = VerificationCode._meta.get_field('created_at')

		self.assertEqual(id_field.primary_key, True)
		self.assertEqual(id_field.default, uuid.uuid4)
		self.assertEqual(id_field.editable, False)
		self.assertEqual(
			code_field.max_length,
			VerificationCode.MAX_CODE_LENGTH
		)
		self.assertEqual(
			created_at_field.auto_now_add,
			True
		)

	def test_manager_create_code_method(self):
		created_verification_code = VerificationCode.objects.create_code(
			email='test@test.pl'
		)

		self.assertEqual(
			created_verification_code.email, 
			'test@test.pl'
		)
		self.assertNotEqual(
			created_verification_code.expiration_at, 
			None
		)
		self.assertEqual(
			len(created_verification_code.code),
			VerificationCode.MAX_CODE_LENGTH
		)
