import uuid
from django.db import models


class Cart(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)

	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE
	)

	products = models.ManyToManyField('elabodeal.Product')

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@property
	def products_count(self):
		return self.products.count()