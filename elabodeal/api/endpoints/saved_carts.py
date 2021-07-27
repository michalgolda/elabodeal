from rest_framework.exceptions import NotFound

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import (
    SaveCartInteractor,
    ShareSavedCartInteractor,
    DeleteSavedCartInteractor
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


class MeSavedCartsEndpoint(Endpoint):
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


class MeShareSavedCartEndpoint(Endpoint):
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


class MeSavedCartsDetailsEndpoint(Endpoint):
    def delete(self, request, id = None):
        user = request.user

        cart_repo = CartRepository()

        interactor = DeleteSavedCartInteractor(
            cart_repo=cart_repo
        )
        deleted_cart = interactor.execute(user, id)

        if not deleted_cart: raise NotFound

        return self.respond(status=200)