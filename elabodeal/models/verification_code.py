import random
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

from elabodeal.models import User
from elabodeal.emails import ConfirmChangeEmail
from elabodeal.celery.tasks import send_email


class VerificationCodeException(Exception):
	pass


class VerificationCodeManager(models.Manager):
	def generate(self, email, expires=86400):		
		user = User.objects.filter(email=email).first()
		if not user:
			raise VerificationCodeException(
				'Not found candidate for that email address'
			)
		
		# Delete code if exist
		verification_code = self.model.objects.filter(email=email).first()
		if verification_code:
			verification_code.delete()

		code = ''.join(str(random.randint(0, 9)) for _ in range(6))
		expiration = timezone.now() + datetime.timedelta(seconds=expires)

		verification_code = self.model(
			code=code,
			email=email,
			expiration_at=expiration
		)
		verification_code.save()

		code = verification_code.code

		confirm_change_email = ConfirmChangeEmail(
			to=verification_code.email,
			context=dict(
				code=verification_code.code
			)
		)
		
		send_email.delay(
			email=confirm_change_email.asdict()
		)

		return verification_code

	def verify(self, email, code):
		verification_code = self.model.objects.filter(email=email).first()
	
		# Check whether verification code is exist for that email address
		if not verification_code:
			raise VerificationCodeException(
				'Not found verification code for that email address'
			)
		
		current_datetime = timezone.now()
		expiration_datetime = verification_code.expiration_at

		# Check code is valid
		if verification_code.code != code:
			raise VerificationCodeException(
				'Verification code is invalid'
			)

		# Check expiration
		if current_datetime > expiration_datetime:
			verification_code.delete()

			raise VerificationCodeException(
				'Verification code is expired'
			)

		user = User.objects.filter(email=email).first()
		user.email_verified = True
		user.email_verified_at = timezone.now()
		user.save()

		# Delete code after verification
		verification_code.delete()

		return user


class VerificationCode(models.Model):
	code = models.CharField(max_length=6)
	email = models.EmailField()
	expiration_at = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = VerificationCodeManager()


