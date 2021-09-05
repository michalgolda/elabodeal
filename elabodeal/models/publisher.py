import uuid
from django.db import models
from django.utils.translation import gettext as _


class PublisherManager(models.Manager):
	def create_publisher(
		self, first_name, 
		last_name, account_number, swift
	):
		publisher = self.model(
			first_name=first_name, 
			last_name=last_name,
			swift=swift, 
			account_number=account_number, 
		)
		publisher.save()

		return publisher


class Publisher(models.Model):
	MAX_SWIFT_LENGHT = 8
	MAX_BIO_LENGTH = 300
	MAX_LAST_NAME_LENGTH = 30
	MAX_FIRST_NAME_LENGTH = 30
	MAX_WHO_YOU_ARE_LENGTH = 30
	MAX_BANNER_TEXT_LENGTH = 100
	MAX_ACCOUNT_NUMBER_LENGTH = 26

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	followers = models.ManyToManyField(
		'elabodeal.User', 
		related_name='user_followers'
	)
	first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH)
	last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH)
	account_number = models.CharField(max_length=MAX_ACCOUNT_NUMBER_LENGTH)
	swift = models.CharField(max_length=MAX_SWIFT_LENGHT)
	banner_text = models.CharField(
		null=True,
		default=None,
		max_length=MAX_BANNER_TEXT_LENGTH
	)
	banner_product = models.ForeignKey(
		'elabodeal.Product',
		null=True,
		default=None,
		related_name='banner_product',
		on_delete=models.CASCADE
	)
	avatar_img = models.ForeignKey(
		'elabodeal.File',
		null=True,
		default=None,
		related_name='avatar_img',
		on_delete=models.CASCADE
	)
	banner_img = models.ForeignKey(
		'elabodeal.File',
		null=True,
		default=None,
		related_name='banner_img',
		on_delete=models.CASCADE
	)
	who_you_are = models.CharField(
		null=True,
		default=None,
		max_length=MAX_WHO_YOU_ARE_LENGTH
	)
	bio = models.CharField(
		null=True,
		default=None,
		max_length=MAX_BIO_LENGTH
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = PublisherManager()

	class Meta:
		verbose_name = _('Wydawca')
		verbose_name_plural = _('Wydawcy')

	@property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'
	
	def __str__(self):
		return str(self.id)