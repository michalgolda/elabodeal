import random
import datetime

from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string


class VerificationCodeManager(models.Manager):
	def generate(self, email, expires = 86400):		
		
		expiration = timezone.now() + datetime.timedelta(seconds=expires)

		verification_code = self.model(email=email, 
									   expiration_at=expiration)
		verification_code.code = ''.join(str(random.randint(0, 9)) for _ in range(6))
		verification_code.save()

		# TODO: Dodanie taska wysyłającego email (Celery)
		# Wysłanie wygenerowanego kodu weryfikacyjnego na podany email
        # TODO: Przepisanie wysyłania maila używając sygnałów
		send_mail(
			subject='Elabodeal - Weryfikacja konta',
			message=f'To jest twój kod weryfikacyjny {verification_code.code}',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[verification_code.email],
			html_message=render_to_string('emails/verification.html', 
										  {'code': verification_code.code})
		)

		return verification_code

	def verify(self, user, code):
		verify_code = self.model.objects.filter(email=user.email).first()

		if not verify_code:
			return False

		if verify_code.code != code:
			return False
		
		curr_datetime = timezone.now()
		if curr_datetime > verify_code.expiration_at:
			# Usunięcie kodu z bazy danych, który stracił ważność
			verify_code.delete()
			
			return False

		user.email_verified = True
		user.email_verified_at = timezone.now()
		user.save()

		# Jeżeli kod został zweryfikowany, zostaje usunięty z bazy danych
		verify_code.delete()

		return True


class VerificationCode(models.Model):
	code = models.CharField(max_length=6)
	email = models.EmailField()
	expiration_at = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = VerificationCodeManager()


