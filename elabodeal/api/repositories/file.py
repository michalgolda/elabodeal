from elabodeal.api.repositories import Repository
from elabodeal.models import File


class FileRepository(Repository):

	def add(self, uploaded_memory_file, type):
		return File.objects.create_file(uploaded_memory_file, type)

	def get_one_by(self, *args, **kwargs):
		return File.objects.filter(*args, **kwargs).first()

	def get_all_by(self, *args, **kwargs):
		return File.objects.filter(*args, **kwargs).all()

	def delete_by(self, *args, **kwargs):
		return File.objects.filter(*args, **kwargs).delete()