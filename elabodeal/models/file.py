import uuid
import hashlib

from pathlib import Path

from django.db import models
from django.templatetags.static import static
from django.utils.translation import gettext as _
from django.core.files.storage import DefaultStorage


class FileManager(models.Manager):

	def create_file(self, uploaded_memory_file, type):
		storage = DefaultStorage()

		extension = Path(uploaded_memory_file.name).suffix.replace('.', '') 
		size = uploaded_memory_file.size
		hash = hashlib.md5(uploaded_memory_file.read()).hexdigest()

		file = self.model(
			size=size,
			hash=hash,
			type=type,
			extension=extension
		)

		name = f'{str(file.id)}.{extension}'

		file.path = static(f'media/{name}')
		file.save()

		storage.save(
			name,
			uploaded_memory_file 
		)

		return file


class File(models.Model):

	class Extension(models.TextChoices):
		JPG = 'jpg'
		PNG = 'png'
		EPUB = 'epub'
		MOBI = 'mobi'
		PDF = 'pdf'

	class Type(models.TextChoices):
		IMAGE = 'img'
		COVER = 'cover'
		EBOOK = 'ebook'

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

	objects = FileManager()

	class Meta:
		verbose_name = _('Plik')
		verbose_name_plural = _('Pliki')

	def __str__(self):
		return str(self.id)