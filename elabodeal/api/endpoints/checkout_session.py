from elabodeal.utils import CartSessionManager

from elabodeal.api.interactors import (
    CreateCheckoutSessionInteractor,
	UpdateCheckoutSessionInteractor,
	RemoveCheckoutSessionInteractor,
	SucceedCheckoutSessionInteractor
)
from elabodeal.api.endpoints import Endpoint
from elabodeal.api.services import StripePaymentService
from elabodeal.api.repositories import ProductRepository
from elabodeal.api.serializers import UpdateCheckoutSessionRequestSerializer


class CheckoutSessionEndpoint(Endpoint):
	permission_classes = []

	def post(self, request):
		session = request.session

		cart_manager = CartSessionManager(session)
		payment_service = StripePaymentService()

		interactor = CreateCheckoutSessionInteractor(
			cart_manager=cart_manager,
			payment_service=payment_service
		)
		checkout_session = interactor.execute(session)

		return self.respond(
			data=checkout_session,
			status=201
		)

	def put(self, request):
		serialized_request = UpdateCheckoutSessionRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		session = request.session

		interactor = UpdateCheckoutSessionInteractor()
		checkout_session = interactor.execute(
			session,
			**serialized_request.validated_data
		)

		return self.respond(
			data=checkout_session,
			status=200
		)

	def delete(self, request):
		session = request.session

		payment_service = StripePaymentService()

		interactor = RemoveCheckoutSessionInteractor(
			payment_service=payment_service
		)
		interactor.execute(session)

		return self.respond(status=200)


class SucceedCheckoutSessionEndpoint(Endpoint):
	permission_classes = []
	
	def post(self, request):
		user = request.user
		session = request.session

		product_repo = ProductRepository()
		cart_manager = CartSessionManager(session)

		interactor = SucceedCheckoutSessionInteractor(
			product_repo=product_repo,
			cart_manager=cart_manager
		)
		interactor.execute(
			user,
			session
		)

		return self.respond(status=200)