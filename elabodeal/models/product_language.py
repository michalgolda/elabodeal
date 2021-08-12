import uuid
from django.db import models
from django.utils.translation import gettext as _


class ProductLanguage(models.Model):
	MAX_CODE_LENGTH = 4
	MAX_NAME_LENGTH = 15

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	code = models.CharField(max_length=MAX_CODE_LENGTH)
	name = models.CharField(max_length=MAX_NAME_LENGTH)

	class Meta:
		verbose_name = _('Język produktu')
		verbose_name_plural = _('Języki produktów')

	def __str__(self):
		return str(self.id)