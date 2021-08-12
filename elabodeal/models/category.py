import uuid
from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
	MAX_NAME_LENGTH = 25

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	name = models.CharField(max_length=MAX_NAME_LENGTH)

	class Meta:
		verbose_name = _('Kategoria')
		verbose_name_plural = _('Kategorie')

	def __str__(self):
		return str(self.id)