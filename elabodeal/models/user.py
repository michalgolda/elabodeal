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

	def update_settings(self, user, options):
		has_changed = False

		for attr_name, attr_value in options.items():
			if getattr(user, attr_name) != attr_value and attr_name != None:
				setattr(user, attr_name, attr_value)

				# Force verification for email address
				if attr_name == 'email':
					user.email_verified = False

				has_changed = True

		if not has_changed:
			return

		user.save()

		return user


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