import uuid
from django.db import models


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
	MAX_FIRST_NAME_LENGTH = 30
	MAX_LAST_NAME_LENGTH = 30
	MAX_ACCOUNT_NUMBER_LENGTH = 26
	MAX_SWIFT_LENGHT = 8

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH)
	last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH)
	account_number = models.CharField(max_length=MAX_ACCOUNT_NUMBER_LENGTH)
	swift = models.CharField(max_length=MAX_SWIFT_LENGHT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = PublisherManager()

	def __str__(self):
		return self.full_name

	@property
	def full_name(self) -> str:
		return f'{self.first_name} {self.last_name}'