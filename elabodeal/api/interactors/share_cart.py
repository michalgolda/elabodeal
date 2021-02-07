from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry

from elabodeal.models import SharedCart


class ShareCartInteractor(Interactor):
    def __init__(self, shared_cart_repo: object, cart_repo: object):
        self.shared_cart_repo = shared_cart_repo
        self.cart_repo= cart_repo

    def execute(self, cart_id: int) -> None:
        existing_cart = self.cart_repo.get(id=cart_id)

        shared_cart = SharedCart.objects.create_share(
            cart=existing_cart
        )

        self.shared_cart_repo.save(shared_cart)