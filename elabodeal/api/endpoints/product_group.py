from rest_framework.exceptions import NotFound

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.permissions import PublisherOnlyAccess
from elabodeal.api.interactors import (
	GetProductGroupInteractor,
	GetProductGroupListInteractor,
	CreateProductGroupInteractor,
	DeleteProductGroupInteractor
)
from elabodeal.api.serializers import ProductGroupSerializer
from elabodeal.api.repositories import ProductGroupRepository


class MeProductsGroupsEndpoint(Endpoint):
	permission_classes = [PublisherOnlyAccess]

	def get(self, request):
		publisher = request.user.publisher

		product_group_repo = ProductGroupRepository()

		interactor = GetProductGroupListInteractor(
			product_group_repo=product_group_repo
		)
		product_group_list = interactor.execute(publisher)

		serialized_product_group_list = ProductGroupSerializer(
			product_group_list, 
			many=True
		)

		return self.respond(
			data=serialized_product_group_list.data,
			status=200
		)

	def post(self, request):
		publisher = request.user.publisher

		product_group_repo = ProductGroupRepository()

		interactor = CreateProductGroupInteractor(
			product_group_repo=product_group_repo
		)
		created_product_group = interactor.execute(publisher)

		serialized_product_group = ProductGroupSerializer(created_product_group)

		return self.respond(
			data=serialized_product_group.data,
			status=201
		)


class MeProductsGroupsDetailsEndpoint(Endpoint):
	permission_classes = [PublisherOnlyAccess]

	def get(self, request, product_group_id = None):
		publisher = request.user.publisher

		product_group_repo = ProductGroupRepository()

		interactor = GetProductGroupInteractor(
			product_group_repo=product_group_repo
		)
		product_group = interactor.execute(publisher, product_group_id)

		if not product_group:
			raise NotFound

		serialized_product_group = ProductGroupSerializer(product_group)

		return self.respond(
			data=serialized_product_group.data,
			status=200
		)

	def delete(self, request, product_group_id = None):
		publisher = request.user.publisher

		product_group_repo = ProductGroupRepository()

		interactor = DeleteProductGroupInteractor(
			product_group_repo=product_group_repo
		)
		deleted_product_group = interactor.execute(publisher, product_group_id)

		if not deleted_product_group:
			raise NotFound

		return self.respond(status=200)