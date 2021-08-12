import uuid
from django.db import models
from django.utils.translation import gettext as _


class ProductPremiere(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)

	datetime = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('Premiera produktu')
		verbose_name_plural = _('Premiery produktów')

	def __str__(self):
		return str(self.id)