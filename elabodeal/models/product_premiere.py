import uuid

from django.db import models


class ProductPremiere(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)

	date = models.DateField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)