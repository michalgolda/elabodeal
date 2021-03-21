from elabodeal.api.repositories import Repository
from elabodeal.models import ProductGroup


class ProductGroupRepository(Repository):

	def add(self, *args, **kwargs):
		return ProductGroup.objects.create(*args, **kwargs)

	def get_all_by(self, *args, **kwargs):
		return ProductGroup.objects.filter(*args, **kwargs).all()

	def get_one_by(self, *args, **kwargs):
		return ProductGroup.objects.filter(*args, **kwargs).first()

	def delete_by(self, *args, **kwargs):
		return any(ProductGroup.objects.filter(*args, **kwargs).delete())