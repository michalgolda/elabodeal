from django.db import models


class PublisherManager(models.Manager):
	def create_publisher(
		self, first_name, 
		last_name, account_number, 
		 country, swift, sell_notification = False
	) -> object:

		publisher = self.model(
			first_name=first_name, 
			last_name=last_name,
			account_number=account_number, 
			country=country,
			swift=swift, 
			sell_notification=sell_notification
		)
		publisher.save()

		return publisher


class Publisher(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	account_number = models.CharField(max_length=26)
	country = models.CharField(max_length=3)
	swift = models.CharField(max_length=8)

	sell_notification = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = PublisherManager()

	def __str__(self):
		return self.full_name

	@property
	def full_name(self) -> str:
		return f'{self.first_name} {self.last_name}'