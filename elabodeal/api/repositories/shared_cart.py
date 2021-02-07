from elabodeal.api.repositories import Repository
from elabodeal.models import SharedCart


class SharedCartRepository(Repository):
    def get(self, id: int) -> SharedCart:
        return SharedCart.objects.filter(id=id).first()

    def delete(self, shared_cart: SharedCart) -> None:
        shared_cart.delete()

    def save(self, shared_cart: SharedCart) -> SharedCart:
        shared_cart.save()

        return shared_cart