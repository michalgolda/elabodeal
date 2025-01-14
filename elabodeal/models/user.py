import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
	AbstractBaseUser, 
	BaseUserManager
)
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
	def create_user(self, email, username, password):
		user = self.model(
			email=BaseUserManager.normalize_email(email),
			username=username
		)
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


class User(AbstractBaseUser):
	MAX_USERNAME_LENGTH = 15

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	publisher = models.OneToOneField(
		'elabodeal.Publisher',
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)
	username = models.CharField(max_length=MAX_USERNAME_LENGTH)
	email = models.EmailField(unique=True)
	email_verified = models.BooleanField(default=False)
	email_verified_at = models.DateTimeField(null=True, blank=True)
	followers = models.ManyToManyField('elabodeal.Publisher', related_name='publisher_followers')
	is_staff = models.BooleanField(default=False)
	is_online = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	newsletter = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'users'
		verbose_name = _('Użytkownik')
		verbose_name_plural = _('Użytkownicy')
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = UserManager()

	@property
	def is_publisher(self):
		return self.publisher != None	

	def already_following(self, publisher_id):
		return self.followers.filter(id=publisher_id).exists()

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

	def __str__(self):
		return str(self.id)