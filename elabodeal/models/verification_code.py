import uuid
from random import randint
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class VerificationCodeValidationError(Exception):
	pass


class VerificationCodeManager(models.Manager):
	def create_code(self, email, expires = 3600 * 60 * 60):
		current_datetime = timezone.now()
		code_length = self.model.MAX_CODE_LENGTH

		expiration_timedelta = timedelta(seconds=expires)
		expiration_datetime = current_datetime + expiration_timedelta

		code = ''.join(str(randint(0, 9)) for _ in range(code_length))

		verification_code = self.model(
			email=email,
			code=code,
			expiration_at=expiration_datetime
		)
		verification_code.save()

		return verification_code

	def validate(self, email, code):
		existing_verification_code = self.model.objects.filter(email=email).last()

		if not existing_verification_code:
			raise VerificationCodeValidationError(
				_(
					'Nie znaleziono kodu weryfikacyjnego',
					'przypisanego do podanego adresu email'
				)				
			)

		current_datetime = timezone.now()

		if current_datetime > existing_verification_code.expiration_at:
			raise VerificationCodeValidationError(
				_('Podany kod weryfikacyjny jest nieaktwyny')
			)

		if code != existing_verification_code.code:
			raise VerificationCodeValidationError(
				_('Podany kod weryfikacyjny jest błędny')
			)

		return existing_verification_code


class VerificationCode(models.Model):
	MAX_CODE_LENGTH = 6

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	email = models.EmailField()
	expiration_at = models.DateTimeField()
	code = models.CharField(max_length=MAX_CODE_LENGTH)
	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = VerificationCodeManager()

	class Meta:
		verbose_name = _('Kod weryfikacyjny')
		verbose_name_plural = _('Kody weryfikacyjne')

	def __str__(self):
		return str(self.id)