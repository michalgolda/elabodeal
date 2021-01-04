from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, 
										BaseUserManager)


class UserManager(BaseUserManager):
	def create_user(self, email, username, password):
		user = self.model(email=BaseUserManager.normalize_email(email),
						  username=username)
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(email, username, password)
		user.is_staff = True
		user.is_superuser = True
		user.email_verified = True
		user.email_verified_at = timezone.now()

		user.save()

		return user

	def update_settings(self, user: object, settings: dict) -> None:
		"""Update user specifed settings

		Setting values of user object or publisher object by attributes
		of settings dictionary. If not any change skip and don't save to db.

		Args:
			user:
				A instance of user object
			settings:
				A dictionary of attribiutes and values for update
				instance of user.
		"""

		has_changed = False

		for attr_name, attr_value in settings.items():

			# Zmiana wartości parametru obiektu User
			if hasattr(user, attr_name):
				if getattr(user, atrr_value) != attr_value:
						setattr(user, attr_name, attr_value)

						has_changed = True

			# Zmiana wartości parametrów obiektu Publisher
			elif attr_name.startswith('publisher.'):
				attr_name = attr_name.split('.')[1]

				if hasattr(user.publisher, attr_name):
					if getattr(user.publisher, attr_name) != attr_value:
						setattr(user.publisher, attr_name, attr_value)

						has_changed = True
						
		if not has_changed: return

		user.save()
		user.publisher.save()


class User(AbstractBaseUser):
	publisher = models.OneToOneField('elabodeal.Publisher',
							  		 on_delete=models.CASCADE,
							  		 null=True)

	username = models.CharField(max_length=15)
	email = models.EmailField(unique=True)
	email_verified = models.BooleanField(default=False)
	email_verified_at = models.DateTimeField(null=True)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_online = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'users'
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = UserManager()


	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser