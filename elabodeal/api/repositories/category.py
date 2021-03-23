from elabodeal.api.repositories import Repository
from elabodeal.models import Category


class CategoryRepository(Repository):

	def add(self, *args, **kwargs):
		return Category.objects.create(*args, **kwargs)

	def get_all_by(self, *args, **kwargs):
		return Category.objects.filter(*args, **kwargs).all()

	def get_one_by(self, *args, **kwargs):
		return Category.objects.filter(*args, **kwargs).first()

	def delete_by(self, *args, **kwargs):
		return any(Category.objects.filter(*args, **kwargs).delete())