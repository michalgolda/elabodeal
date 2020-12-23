import os
import uuid

from django.db import models
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage


class FileManager(models.Manager):
	def upload_file(self, file_object):
		if not file_object:
			return

		_uuid = uuid.uuid4()
		size = file_object.size
		
		file_name = file_object.name
		
		extension = os.path.splitext(file_name)[1]
		path = f'/files/{_uuid}{extension}'

		file_name = f'{_uuid}{extension}'

		fs_manager = FileSystemStorage()
		fs_manager.save(file_name, file_object)

		file = self.model(uuid=_uuid,
						  size=size,
						  path=path,
						  extension=extension)
		file.save()

		return file


class File(models.Model):
	uuid = models.CharField(max_length=36)
	size = models.IntegerField()
	path = models.URLField()
	extension = models.CharField(max_length=4)

	uploaded_at = models.DateTimeField(auto_now_add=True)

	objects = FileManager()
	
	@property
	def file_name(self):
		return f'{self.uuid}{self.extension}'

	def __str__(self):
		return self.uuid


@receiver(models.signals.post_delete, sender=File)
def delete_file_from_storage(sender, instance, **kwargs):
	fs_manager = FileSystemStorage()

	fs_manager.delete(instance.file_name)