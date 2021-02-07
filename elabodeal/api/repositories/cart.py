from elabodeal.api.repositories import Repository
from elabodeal.models import Cart


class CartRepository(Repository):
    def get(self, id: int) -> Cart:
        return Cart.objects.filter(id=id).first()

    def delete(self, cart: Cart) -> None:
        cart.delete()

    def save(self, cart: Cart) -> Cart:
        cart.save()