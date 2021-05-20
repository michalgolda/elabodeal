from elabodeal.models import ProductGroup
from elabodeal.api.interactors import Interactor


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

	def execute(self, publisher):
		return self.product_group_repo.add(publisher=publisher)


class DeleteProductGroupInteractor(BaseProductGroupInteractor):

	def execute(self, publisher, product_group_id):
		return self.product_group_repo.delete_by(
			publisher=publisher,
			id=product_group_id
		)