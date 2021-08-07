from rest_framework.exceptions import NotFound

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.permissions import PublisherOnlyAccess
from elabodeal.api.interactors import (
	GetProductInteractor,
	DeleteProductInteractor,
	GetProductListInteractor,
	CreateProductInteractor
)
from elabodeal.api.serializers import (
	ProductSerializer,
	CreateProductRequestSerializer
)
from elabodeal.api.repositories import (
	FileRepository,
	ProductRepository,
	CategoryRepository,
	ProductGroupRepository,
	ProductLanguageRepository,
	ProductPremiereRepository
)


class MeProductsEndpoint(Endpoint):
	permission_classes = [PublisherOnlyAccess]

	def get(self, request):
		publisher = request.user.publisher

		product_repo = ProductRepository()

		interactor = GetProductListInteractor(
			product_repo=product_repo
		)
		product_list = interactor.execute(publisher)

		serialized_product_list = ProductSerializer(product_list, many=True)

		return self.respond(
			data=serialized_product_list.data,
			status=200
		)

	def post(self, request):
		serialized_request = CreateProductRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		user = request.user
		publisher = user.publisher

		file_repo = FileRepository()
		category_repo = CategoryRepository()
		product_repo = ProductRepository()
		product_group_repo = ProductGroupRepository()
		product_language_repo = ProductLanguageRepository()
		product_premiere_repo = ProductPremiereRepository()

		interactor = CreateProductInteractor(
			file_repo=file_repo,
			product_repo=product_repo,
			category_repo=category_repo,
			product_group_repo=product_group_repo,
			product_language_repo=product_language_repo,
			product_premiere_repo=product_premiere_repo
		)
		created_product = interactor.execute(
			user,
			publisher,
			**serialized_request.validated_data
		)

		serialized_product = ProductSerializer(created_product)

		return self.respond(
			data=serialized_product.data,
			status=201
		)


class MeProductsDetailsEndpoint(Endpoint):
	permission_classes = [PublisherOnlyAccess]

	def get(self, request, product_id = None):
		publisher = request.user.publisher

		product_repo = ProductRepository()

		interactor = GetProductInteractor(
			product_repo=product_repo
		)
		product = interactor.execute(publisher, product_id)

		if not product:
			raise NotFound

		serialized_product = ProductSerializer(product)

		return self.respond(
			data=serialized_product.data,
			status=200
		)

	def delete(self, request, product_id = None):
		publisher = request.user.publisher

		product_repo = ProductRepository()

		interactor = DeleteProductInteractor(
			product_repo=product_repo
		)	
		deleted_product = interactor.execute(publisher, product_id)

		if not deleted_product:
			raise NotFound

		return self.respond(status=200)