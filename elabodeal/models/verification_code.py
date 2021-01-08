import random
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string

from elabodeal.models import User


class VerificationCodeManager(models.Manager):
	def generate(self, email: str, expires: int = 86400) -> object:		
		# Delete exist code and generate new
		verification_code = self.model.objects.filter(email=email).first()
		if verification_code:
			verification_code.delete()

		expiration = timezone.now() + datetime.timedelta(seconds=expires)

		verification_code = self.model(email=email, 
									   expiration_at=expiration)
		verification_code.code = ''.join(str(random.randint(0, 9)) for _ in range(6))
		verification_code.save()

		code = verification_code.code
		recipient = verification_code.email
		from_email = settings.EMAIL_HOST_USER
		subject = 'Elabodeal - Weryfikacja konta'
		message = f'To jest twój kod weryfikacyjny {code}'
		html_message = render_to_string('emails/verification.html', 
										{'code': code})

		send_mail(subject=subject,
				  message=message,
				  from_email=from_email,
				  recipient_list=[recipient],
				  html_message=html_message)

		return verification_code

	def verify(self, email: str, code: int) -> object:
		user = User.objects.filter(email=email).first()

		if not user:
			raise ValueError('Not found user by email for verification')

		verify_code = self.model.objects.filter(email=user.email).first()
	
		if not verify_code:
			raise ValueError('Not found verification code')
		elif verify_code.code != code:
			raise ValueError('Verification code is invalid')
		
		curr_datetime = timezone.now()
	
		if curr_datetime > verify_code.expiration_at:
			verify_code.delete()
			
			raise ValueError('Verification code is expired')

		user.email_verified = True
		user.email_verified_at = timezone.now()
		user.save()

		verify_code.delete()

		return user


class VerificationCode(models.Model):
	code = models.CharField(max_length=6)
	email = models.EmailField()
	expiration_at = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = VerificationCodeManager()


