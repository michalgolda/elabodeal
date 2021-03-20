import uuid
from django.db import models


class ProductGroup(models.Model):
	MAX_NAME_LENGTH = 50

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	publisher = models.ForeignKey(
		'elabodeal.Publisher',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=MAX_NAME_LENGTH)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)