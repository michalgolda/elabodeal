from elabodeal.models import ProductGroup
from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ResourceIsAlreadyExists


class BaseProductGroupInteractor(Interactor):

	def __init__(self, product_group_repo):
		self.product_group_repo = product_group_repo


class GetProductGroupListInteractor(BaseProductGroupInteractor):

	def execute(self, publisher):
		return self.product_group_repo.get_all_by(publisher=publisher)


class GetProductGroupInteractor(BaseProductGroupInteractor):

	def execute(self, publisher, product_group_id):
		return self.product_group_repo.get_one_by(
			publisher=publisher,
			id=product_group_id
		)


class CreateProductGroupInteractor(BaseProductGroupInteractor):

	def execute(self, publisher, name):
		existing_product_group = self.product_group_repo.get_one_by(
			name=name,
			publisher=publisher
		)
		if existing_product_group:
			raise ResourceIsAlreadyExists('The product group with this name is already exists.')

		return self.product_group_repo.add(
			publisher=publisher,
			name=name
		)


class DeleteProductGroupInteractor(BaseProductGroupInteractor):

	def execute(self, publisher, product_group_id):
		return self.product_group_repo.delete_by(
			publisher=publisher,
			id=product_group_id
		)