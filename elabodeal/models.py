from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email: str, username: str, password: str):
		if email:
			user = self.model(
				email=self.normalize_email(email),
				username=username
			)

			user.set_password(password)
			user.save(using=self._db)

			return user
		
		raise ValueError('User email address is required')

	def create_staffuser(self, email: str, username: str, password: str):
		user = self.create_user(
				email=self.normalize_email(email),
				username=username,
				password=password			
			)

		user.is_staff = True

		user.save(using=self._db)

		return user

	def create_superuser(self, email: str, username: str, password: str):
		user = self.create_user(
				email=self.normalize_email(email),
				username=username,
				password=password
			)

		user.is_staff = True
		user.is_superuser = True

		user.save(using=self._db)
		
		return user


class User(AbstractBaseUser):
	objects = UserManager()

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)

	email = models.EmailField(max_length=256, unique=True)
	email_verified = models.BooleanField(default=False)
	email_verified_at = models.DateTimeField(null=True)

	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		db_table = 'users'

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser


class VerifyCode(models.Model):
	email = models.EmailField(max_length=256)
	code = models.CharField(max_length=6)
	created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return f'{self.name}'


class Product(models.Model):
	category = models.ForeignKey('elabodeal.Category', on_delete=models.CASCADE, related_name='product_category')
	author = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE, related_name='product_author')

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	price =	models.DecimalField(max_digits=4, decimal_places=2)
	cover_img_url = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)