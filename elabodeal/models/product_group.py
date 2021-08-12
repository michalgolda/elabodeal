import uuid
from django.db import models
from django.utils.translation import gettext as _


class ProductGroup(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	publisher = models.ForeignKey(
		'elabodeal.Publisher',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('Grupa produktów')
		verbose_name_plural = _('Grupy produktów')

	def __str__(self):
		return str(self.id)