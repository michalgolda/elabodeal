import datetime

from tests.base import TestCase

from django.core import mail
from django.conf import settings
from django.utils import timezone

from elabodeal.models import VerificationCode


class TestVerificationCodeModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(VerificationCode, 'code'), True)
		self.assertEqual(hasattr(VerificationCode, 'email'), True)
		self.assertEqual(hasattr(VerificationCode, 'expiration_at'), True)
		self.assertEqual(hasattr(VerificationCode, 'created_at'), True)

	def test_manager_generate_method(self):
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		__verify_code = VerificationCode.objects.filter(email='xyz@xyz.pl').first()
		
		self.assertNotEqual(__verify_code, None)
		self.assertEqual(__verify_code.code, verify_code.code)
		self.assertEqual(len(verify_code.code), 6)

	def test_manager_generate_method_send_email(self):
		settings.EMAIL_HOST_USER = 'abc@abc.pl'
		
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].subject , 'Elabodeal - Weryfikacja konta')
		self.assertIn(verify_code.code, mail.outbox[0].body)

	def test_manager_verify_method(self):
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		is_verified = VerificationCode.objects.verify(code=verify_code.code, email=verify_code.email)
		self.assertEqual(is_verified, True)

	def test_manager_verify_method_if_email_does_not_valid(self):
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		is_verified = VerificationCode.objects.verify(code=verify_code.code, email='')
		self.assertEqual(is_verified, False)

	def test_manager_verify_method_if_code_does_not_valid(self):
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		is_verified = VerificationCode.objects.verify(code='', email='xyz@xyz.pl')
		self.assertEqual(is_verified, False)

	def test_manager_verify_method_if_code_is_expired(self):
		verify_code = VerificationCode.objects.generate(email='xyz@xyz.pl')

		verify_code.expiration_at = timezone.now() - datetime.timedelta(hours=24)
		verify_code.save()

		is_verified = VerificationCode.objects.verify(code=verify_code.code, email=verify_code.email)
		self.assertEqual(is_verified, False)

		# Sprawdzenie czy kod, który stracił ważność został usunięty z bazy danych
		__verify_code = VerificationCode.objects.filter(email=verify_code.email).first()
		self.assertEqual(__verify_code, None)
