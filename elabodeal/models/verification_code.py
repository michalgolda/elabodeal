from random import randint
from datetime import timedelta

from django.db import models
from django.utils import timezone


class VerificationCodeManager(models.Manager):
	def create_code(self, email: str, expires: int = 86400) -> object:
		current_datetime = timezone.now()
		expiration_datetime = current_datetime + timedelta(seconds=expires)
	
		code = ''.join(str(randint(0, 9)) for _ in range(6))

		verification_code = self.model(
			email=email,
			code=code,
			expiration_at=expiration_datetime
		)
		verification_code.save()

		return verification_code


class VerificationCode(models.Model):
	code = models.CharField(max_length=6)
	email = models.EmailField()
	expiration_at = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = VerificationCodeManager()