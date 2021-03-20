import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class File(models.Model):

	class Extension(models.TextChoices):
		JPG = 'jpg'
		PNG = 'png'
		EPUB = 'epub'
		MOBI = 'mobi'
		PDF = 'pdf'

	class Type(models.TextChoices):
		IMAGE = 'img', _('This type is realted to other product images')
		COVER = 'cover', _('This type is related to image which is ebook cover')
		EBOOK = 'ebook', _('This type is realted to all supported ebook extension files')

	MAX_EXTENSION_LENGTH = 4
	MAX_TYPE_LENGTH = 5
	MAX_HASH_LENGTH = 32

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	size = models.IntegerField()
	path = models.URLField()
	extension = models.CharField(
		max_length=MAX_EXTENSION_LENGTH,
		choices=Extension.choices
	)
	type = models.CharField(
		max_length=MAX_TYPE_LENGTH,
		choices=Type.choices
	)
	hash = models.CharField(max_length=MAX_HASH_LENGTH)
	uploaded_at = models.DateTimeField(auto_now_add=True)