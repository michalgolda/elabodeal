from elabodeal.api.repositories import Repository
from elabodeal.models import Cart


class CartRepository(Repository):
    def add(self, *args, **kwargs):
        return Cart.objects.create(*args, **kwargs)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())
    
    def save(self, cart):
        cart.save()

        return cart

    def _query_filter(self, *args, **kwargs):
        return Cart.objects.filter(*args, **kwargs)