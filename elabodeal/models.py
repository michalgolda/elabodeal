import uuid
import json

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage


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
	is_seller = models.BooleanField(default=False)

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


class AgeCategory(models.Model):
	value = models.IntegerField()

	def __str__(self):
		return f'{self.value}+'


class File(models.Model):
	size = models.IntegerField()
	url = models.URLField()
	mime = models.CharField(max_length=30)
	name = models.CharField(max_length=150)
	extension = models.CharField(max_length=4)
	uploaded_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
	category = models.ForeignKey('elabodeal.Category', on_delete=models.CASCADE, related_name='product_category')
	user = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE, related_name='product_user')

	pdf = models.ForeignKey('elabodeal.File', on_delete=models.CASCADE, null=True, related_name='product_pdf_file')
	epub = models.ForeignKey('elabodeal.File', on_delete=models.CASCADE, null=True, related_name='product_epub_file')
	mobi = models.ForeignKey('elabodeal.File', on_delete=models.CASCADE, null=True, related_name='product_mobi_file')
	cover_img = models.ForeignKey('elabodeal.File', on_delete=models.CASCADE, null=True, related_name='product_cover_img_file')

	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	price =	models.DecimalField(max_digits=10, decimal_places=2)
	page_count = models.IntegerField()
	isbn = models.CharField(max_length=13)
	age_categories = models.ManyToManyField(AgeCategory, blank=True, related_name='product_age_category')
	contents = models.CharField(max_length=400, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def set_age(self, value):
		if not value in [3, 7, 12, 16, 18]: 
			raise ValueError(f'Value {value} is invalid.')

		age_category = AgeCategory.objects.filter(value=value).first()
		if not age_category:
			age_category = AgeCategory(value=value)

		self.age_categories.add(age_category)

	def set_pdf(self, file):
		name = uuid.uuid4()
		content_type = file.content_type
		extension = content_type[-3:]
		full_name = f'{name}.{extension}'
		url = f'/api/files/{full_name}/'
		pdf = self.add_file(
			uuid.uuid4(),
			extension,
			content_type,
			file.size,
			url
		)
		self.pdf = pdf
		self.save()

		file_storage = FileSystemStorage()
		file_storage.save(full_name, file)

	def set_mobi(self, file):
		name = uuid.uuid4()
		content_type = file.content_type
		extension = content_type[-3:]
		full_name = f'{name}.{extension}'
		url = f'/api/files/{full_name}/'
		mobi = self.add_file(
			uuid.uuid4(),
			extension,
			content_type,
			file.size,
			url
		)
		self.mobi = mobi
		self.save()

		file_storage = FileSystemStorage()
		file_storage.save(full_name, file)

	def set_epub(self, file):
		name = uuid.uuid4()
		content_type = file.content_type
		extension = content_type[-3:]
		full_name = f'{name}.{extension}'
		url = f'/api/files/{full_name}/'
		epub = self.add_file(
			uuid.uuid4(),
			extension,
			content_type,
			file.size,
			url
		)
		self.epub = epub
		self.save()

		file_storage = FileSystemStorage()
		file_storage.save(full_name, file)

	def set_cover_img(self, file):
		name = uuid.uuid4()
		content_type = file.content_type
		extension = content_type.split('image/')[1]
		full_name = f'{name}.{extension}'
		url = f'/static/cover_images/{full_name}'
		cover_img = self.add_file(
			uuid.uuid4(),
			extension,
			content_type,
			file.size,
			url
		)
		self.cover_img = cover_img
		self.save()

		file_storage = FileSystemStorage(location=f'{settings.BASE_DIR}/elabodeal/web/static/cover_images/')
		file_storage.save(full_name, file)

	def add_file(self, name: str, extension: str, mime: str, size: int, url: str) -> File:
		file = File(
			name=name,
			extension=extension,
			mime=mime,
			size=size,
			url=url
		)
		file.save()

		return file

class Cart(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	user = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE, related_name='cart_user')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	
class CartItem(models.Model):
	cart = models.ForeignKey('elabodeal.Cart', on_delete=models.CASCADE, related_name='cart_item_cart')
	product = models.ForeignKey('elabodeal.Product', on_delete=models.CASCADE, related_name='cart_item_product')


class PurchasedProduct(models.Model):
	user = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE)
	product = models.ForeignKey('elabodeal.Product', on_delete=models.CASCADE)