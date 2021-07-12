from django.db import models


class Cart(models.Model):
	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE
	)

	products = models.ManyToManyField('elabodeal.Product')

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)