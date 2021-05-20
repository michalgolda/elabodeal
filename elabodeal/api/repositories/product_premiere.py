from elabodeal.models import ProductPremiere
from elabodeal.api.repositories import Repository


class ProductPremiereRepository(Repository):

	def add(self, *args, **kwargs):
		return ProductPremiere.objects.create(*args, **kwargs)

	def get_all_by(self, *args, **kwargs):
		return ProductPremiere.objects.filter(*args, **kwargs).all()

	def get_one_by(self, *args, **kwargs):
		return ProductPremiere.objects.filter(*args, **kwargs).first()

	def delete_by(self, *args, **kwargs):
		return any(ProductGroup.objects.filter(*args, **kwargs).delete())