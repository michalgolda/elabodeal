from elabodeal.api.endpoints import Endpoint
from elabodeal.api.repositories import ProductRepository
from elabodeal.api.interactors import (
	AddProductToCartInteractor,
	RemoveProductFromCartInteractor
)
from elabodeal.api.serializers import (
	ProductSerializer,
	UpdateCartRequestSerializer
)
from elabodeal.utils import CartSessionManager


class MeUpdateCartEndpoint(Endpoint):
	permission_classes = []
	authentication_classes = []

	def put(self, request):
		session = request.session

		serialized_request = UpdateCartRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		product_repo = ProductRepository()
		cart_manager = CartSessionManager(session)

		interactor = AddProductToCartInteractor(
			cart_manager=cart_manager,
			product_repo=product_repo,
		)
		
		product = interactor.execute(
			**serialized_request.validated_data
		)

		serialized_product = ProductSerializer(product)

		return self.respond(
			data=serialized_product.data,
			status=200
		)

	def delete(self, request):
		session = request.session

		serialized_request = UpdateCartRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		cart_manager = CartSessionManager(session)

		interactor = RemoveProductFromCartInteractor(
			cart_manager=cart_manager
		)
		interactor.execute()

		return self.respond(status=200)



