import datetime
from unittest import skip

from tests.base import TestCase

from django.core import mail
from django.conf import settings
from django.utils import timezone

from elabodeal.models import (
	VerificationCode, 
	VerificationCodeException,
	User
)


class TestVerificationCodeModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(VerificationCode, 'code'), True)
		self.assertEqual(hasattr(VerificationCode, 'email'), True)
		self.assertEqual(hasattr(VerificationCode, 'expiration_at'), True)
		self.assertEqual(hasattr(VerificationCode, 'created_at'), True)

	def test_manager_generate_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		generated_code = VerificationCode.objects.generate(
			email=user.email
		)
		
		self.assertEqual(len(generated_code.code), 6)
		self.assertIsInstance(generated_code, VerificationCode)

		code = VerificationCode.objects.filter(email=user.email).first()
		
		self.assertEqual(generated_code.code, code.code)

	def test_manager_generate_method_not_found_candiate(self):
		with self.assertRaises(VerificationCodeException):
			VerificationCode.objects.generate(
				email='xyz@xyz.pl'
			)

	def test_manager_generate_method_clear_exist_code(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		generated_code_old = VerificationCode.objects.generate(
			email=user.email
		)
			
		generated_code_new = VerificationCode.objects.generate(
			email=user.email
		)

		codes = VerificationCode.objects.filter(email=generated_code_old.email).all()

		self.assertEqual(len(codes), 1)

	def test_manager_generate_method_send_email(self):
		settings.EMAIL_HOST_USER = 'xyz@xyz.pl'
		
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		code = VerificationCode.objects.generate(email=user.email)

		outbox = mail.outbox

		mail_obj = outbox[0]
		mail_subject = mail_obj.subject
		mail_body = mail_obj.body

		self.assertEqual(len(outbox), 1)
		self.assertEqual(mail_subject , 'Elabodeal - Weryfikacja konta')
		self.assertIn(code.code, mail_body)

	def test_manager_verify_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		code = VerificationCode.objects.generate(
			email=user.email
		)

		verified_user = VerificationCode.objects.verify(
			email=code.email, 
			code=code.code
		)
		
		self.assertIsInstance(verified_user, User)
		self.assertEqual(verified_user.email_verified, True)	

	def test_manager_verify_method_not_found_user(self):
		with self.assertRaises(VerificationCodeException):
			VerificationCode.objects.verify(
				email='xyz@xyz.pl', 
				code=123
			)


	def test_manager_verify_method_not_found_code(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		with self.assertRaises(VerificationCodeException):
			VerificationCode.objects.verify(
				email='xyz@xyz.pl', 
				code=123
			)

	def test_manager_verify_method_invalid_code(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)

		code = VerificationCode.objects.generate(
			email=user.email
		)

		with self.assertRaises(VerificationCodeException):
			VerificationCode.objects.verify(
				email=user.email, 
				code=123
			)

	def test_manager_verify_method_expired_code(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz',
			password='xyz'
		)
		
		code = VerificationCode.objects.generate(
			email=user.email
		)
		
		code.expiration_at = timezone.now() - datetime.timedelta(hours=24)
		code.save()

		with self.assertRaises(VerificationCodeException):
			VerificationCode.objects.verify(
				email=code.email, 
				code=code.code
			)