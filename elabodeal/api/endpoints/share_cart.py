from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import ShareCartInteractor
from elabodeal.api.repositories import CartRepository, SharedCartRepository


class ShareCartEndpoint(Endpoint):
    def post(self, request, id: int):
        cart_repository = CartRepository()
        shared_cart_repository = SharedCartRepository()

        with ShareCartInteractor(
            shared_cart_repo=shared_cart_repository,
            cart_repo=cart_repository
        ) as interactor:
            interactor.execute(cart_id=id)

        return self.respond(status=200)