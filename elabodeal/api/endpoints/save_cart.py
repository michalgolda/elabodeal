from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import SaveCartInteractor
from elabodeal.api.repositories import CartRepository, ProductRepository
from elabodeal.api.serializers import SaveCartRequestSerializer


class SaveCartEndpoint(Endpoint):
	def post(self, request):
		serializer = SaveCartRequestSerializer(
			data=request.data
		)
		serializer.is_valid(raise_exception=True)

		cart_session = request.session.get('cart')

		cart_repository = CartRepository()
		product_repository = ProductRepository()

		with SaveCartInteractor(
			cart_repo=cart_repository,
			product_repo=product_repository
		) as interactor:
			interactor.execute(
				cart_session=cart_session,
				user=request.user,
				**serializer.data
			)

		return self.respond(status=200)