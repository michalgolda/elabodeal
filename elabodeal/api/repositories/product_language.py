from elabodeal.api.repositories import Repository
from elabodeal.models import ProductLanguage


class ProductLanguageRepository(Repository):

	def add(self, *args, **kwargs):
		raise NotImplementedError

	def get_one_by(self, *args, **kwargs):
		return ProductLanguage.objects.filter(*args, **kwargs).first()

	def get_all_by(self, *args, **kwargs):
		return ProductLanguage.objects.filter(*args, **kwargs).all()

	def delete_by(self, *args, **kwargs):
		raise NotImplementedError