from django.db import models


class BannedUserManager(models.Manager):
	def ban(self, user, reason):
		banned_user = self.model(user=user, reason=reason)
		banned_user.save()

		# TODO: Dodanie taska wysyłającego email (Celery)
		# TODO: Dodanie szablonu maila
		# Wysyłanie powiadomienia na maila o zablokowanym koncie
		send_mail(
			subject='Elabodeal - Blokada konta',
			message=f'Twoje konto zostało zablokowane. Powód: {banned_user.reason}',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[banned_user.user.email]
		)

		return banned_user

	def unban(self, user):
		banned_user = self.model.objects.filter(user__id=user_id).first()
		if not banned_user:
			raise self.model.DoesNotExist('Nie znaleziono zbanowanego użytkownika o podanym id')

		banned_user.delete()
		# TODO: Dodanie taska wysyłającego email (Celery)
		# TODO: Dodanie szablony maila
        # TODO: Przepisanie wysyłania maila używając sygnałów
		# Wysłanie powiadomienia na maila o odblokwaniu konta
		send_mail(
			subject='Elabodeal - Odblokowano konto',
			message=f'Twoje konto {banned_user.email} zostało odblokowane.',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[banned_user.email]
		)

		return banned_user
		

class BannedUser(models.Model):
	user = models.OneToOneField('elabodeal.User', 
								on_delete=models.CASCADE)

	reason = models.CharField(max_length=150)
	banned_at = models.DateTimeField(auto_now_add=True)

	objects = BannedUserManager()