from elabodeal.api.endpoints import Endpoint
from elabodeal.api.repositories import (
	CartRepository,
	ProductRepository
)
from elabodeal.api.interactors import (
	SaveCartInteractor,
	AddProductToCartInteractor,
	RemoveProductFromCartInteractor
)
from elabodeal.api.serializers import (
	ProductSerializer,
	SaveCartRequestSerializer,
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
			data={
				'product': serialized_product.data,
				'cart': {
					'total_price': cart_manager.total_price,
					'product_count': cart_manager.product_count
				}
			},
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
		interactor.execute(**serialized_request.validated_data)

		return self.respond(
			data={
				'cart': {
					'total_price': cart_manager.total_price,
					'product_count': cart_manager.product_count
				}
			},
			status=200
		)


class MeSaveCartEndpoint(Endpoint):
	def post(self, request):
		user = request.user
		session = request.session

		serialized_request = SaveCartRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		cart_repo = CartRepository()
		product_repo = ProductRepository()
		cart_manager = CartSessionManager(session)

		interactor = SaveCartInteractor(
			cart_repo=cart_repo,
			product_repo=product_repo,
			cart_manager=cart_manager
		)

		interactor.execute(
			user,
			**serialized_request.validated_data
		)

		return self.respond(status=201)