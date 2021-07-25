from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import (
    SaveCartInteractor,
    ShareSavedCartInteractor
)
from elabodeal.api.repositories import (
    CartRepository,
    ProductRepository,
    SharedCartRepository
)
from elabodeal.api.serializers import (
    SharedCartSerializer,
    SaveCartRequestSerializer
)
from elabodeal.utils import CartSessionManager


class SavedCartsEndpoint(Endpoint):
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


class ShareSavedCartEndpoint(Endpoint):
    def post(self, request, id):
        cart_repo = CartRepository()
        shared_cart_repo = SharedCartRepository()

        interactor = ShareSavedCartInteractor(
            cart_repo=cart_repo,
            shared_cart_repo=shared_cart_repo
        )
        shared_cart = interactor.execute(id)

        serialized_shared_cart = SharedCartSerializer(shared_cart)

        return self.respond(
            data=serialized_shared_cart.data,
            status=201
        )