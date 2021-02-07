from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry
from elabodeal.models import Cart


class SaveCartInteractor(Interactor):
    def __init__(self, cart_repo: object, product_repo: object):
        self.cart_repo = cart_repo
        self.product_repo = product_repo

    def execute(self, title: str, description: str, cart_session: dict, user: object) -> None:
        if not cart_session:
            raise ErrorRegistry.SAVE_CART(
                'Session object does not have cart object'
            )

        cart = Cart(
            user=user,
            title=title,
            description=description
        )

        for item in cart_session['items']:
            product = self.product_repo.get(id=item.id)

            cart.items.add(product)

        self.cart_repo.save(cart)

        

        
