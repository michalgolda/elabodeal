import uuid
import json
import random
import string
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, username, password):
		if not email:
			raise ValueError('Adres email jest wymagany')
		
		if not username:
			raise ValueError('Nazwa użytkownika jest wymagana')

		user = self.model(
			email=BaseUserManager.normalize_email(email), 
			username=username)
		user.set_password(password)
		
		user.save()

		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(email, username, password)
		user.is_staff = True
		user.is_superuser = True

		user.save()

		return user

		
class User(AbstractBaseUser):
	class Meta:
		db_table = 'users'
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = UserManager()

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

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser


class BannedUserManager(models.Manager):
	def ban(self, user_id, reason):
		user = User.objects.filter(id=user_id).first()
		if not user:
			raise self.model.DoesNotExist('Nie znaleziono użytkownika o podanym id')

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

	def unban(self, user_id):
		banned_user = User.objects.filter(id=user_id).first()
		if not banned_user:
			raise self.model.DoesNotExist('Nie znaleziono zbanowanego użytkownika o podanym id')

		banned_user.delete()
		# TODO: Dodanie taska wysyłającego email (Celery)
		# TODO: Dodanie szablony maila
		# Wysłanie powiadomienia na maila o odblokwaniu konta
		send_mail(
			subject='Elabodeal - Odblokowano konto',
			message=f'Twoje konto {banned_user.email} zostało odblokowane.',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[banned_user.email]
		)

		return banned_user
		

class BannedUser(models.Model):
	objects = BannedUserManager()

	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE)

	reason = models.CharField(max_length=150)
	banned_at = models.DateTimeField(auto_now_add=True)


class Publisher(models.Model):
	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE)
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	account_number = models.CharField(max_length=26)
	country = models.CharField(max_length=3)
	swift = models.CharField(max_length=8)

	sell_notification = models.BooleanField(default=False)


class VerificationCodeManager(models.Manager):
	def generate(self, email, expires = 86400):		
		verification_code = self.model(
			email=email, 
			expiration_at=timezone.now() + datetime.timedelta(seconds=expires))
		verification_code.code = ''.join(str(random.randint(0, 9)) for _ in range(6))
		verification_code.save(using=self._db)

		# TODO: Dodanie taska wysyłającego email (Celery)
		# Wysłanie wygenerowanego kodu weryfikacyjnego na podany email
		send_mail(
			subject='Elabodeal - Weryfikacja konta',
			message=f'To jest twój kod weryfikacyjny {verification_code.code}',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[verification_code.email],
			html_message=render_to_string('emails/verification.html', {'code': verification_code.code})
		)

		return verification_code

	def verify(self, code, email):
		verify_code = self.model.objects.filter(email=email).first()
		if not verify_code:
			return False

		if verify_code.code != code:
			return False
		
		curr_datetime = timezone.now()
		if curr_datetime > verify_code.expiration_at:
			# Usunięcie kodu z bazy danych, który stracił ważność
			verify_code.delete()
			
			return False

		# Jeżeli kod został zweryfikowany, zostaje usunięty z bazy danych
		verify_code.delete()

		return True


class VerificationCode(models.Model):
	objects = VerificationCodeManager()

	code = models.CharField(max_length=6)
	email = models.EmailField()
	expiration_at = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)


class ProductLabel(models.Model):
	name = models.CharField(max_length=25)
	color = models.CharField(max_length=6, default='#FF9F1C')


class ProductOpinion(models.Model):
	user = models.ForeignKey(
		'elabodeal.User',
		on_delete=models.CASCADE)

	content = models.CharField(max_length=100)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
	publisher = models.ForeignKey(
		'elabodeal.Publisher', 
		on_delete=models.CASCADE)
	
	category = models.ForeignKey(
		'elabodeal.Category', 
		on_delete=models.CASCADE)

	labels = models.ManyToManyField(ProductLabel)
	opinions = models.ManyToManyField(ProductOpinion)

	title = models.CharField(max_length=50)
	description = models.CharField(max_length=400)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	author = models.CharField(max_length=30)
	page_count = models.IntegerField()
	isbn = models.CharField(max_length=13)
	contents = models.CharField(max_length=200, null=True)
	age_category = models.IntegerField()
	url_name = models.CharField(max_length=100)
	average_rating = models.FloatField(default=0)
	rating_count = models.IntegerField(default=0)

	cover_img = models.ForeignKey(
		'elabodeal.File', 
		on_delete=models.CASCADE,
		related_name='cover_img')

	pdf_file = models.ForeignKey(
		'elabodeal.File', 
		on_delete=models.CASCADE,
		related_name='pdf')

	epub_file = models.ForeignKey(
		'elabodeal.File', 
		on_delete=models.CASCADE,
		related_name='epub')

	mobi_file = models.ForeignKey(
		'elabodeal.File', 
		on_delete=models.CASCADE,
		related_name='mobi')

	published_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
	class Meta:
		verbose_name_plural = 'categories'

	name = models.CharField(max_length=25)

	def __str__(self):
		return f'{self.name}'


class File(models.Model):
	uuid = models.CharField(max_length=36)
	size = models.IntegerField()
	url = models.URLField()
	extension = models.CharField(max_length=4)
	uploaded_at = models.DateTimeField(auto_now_add=True)


class SharedCart(models.Model):
	uuid = models.CharField(max_length=36)
	cart = models.ForeignKey(
		'elabodeal.Cart', 
		on_delete=models.CASCADE)

	shared_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
	product = models.ForeignKey(
		'elabodeal.Product', 
		on_delete=models.CASCADE)


class CartManager(models.Manager):
	def share(self, cart_id):
		cart = self.model.objects.filter(id=cart_id).first()
		if not cart:
			raise self.model.DoesNotExist('Nie znaleziono koszyka o podanym id')

		shared_cart = SharedCart.objects.create(
			uuid=uuid.uuid4(), 
			cart=cart)

		return shared_cart


class Cart(models.Model):
	objects = CartManager()
	
	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE)

	items = models.ManyToManyField(CartItem)

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class PurchasedProduct(models.Model):
	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE)
	
	product = models.ForeignKey(
		'elabodeal.Product', 
		on_delete=models.CASCADE)
	
	rating = models.FloatField(default=0)
	has_rating = models.BooleanField(default=False)

	purchased_at = models.DateTimeField(auto_now_add=True)