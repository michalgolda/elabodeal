from elabodeal.api.repositories import Repository
from elabodeal.models import SharedCart


class SharedCartRepository(Repository):
    def add(self, cart):
        return SharedCart.objects.create_shared_cart(cart)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())

    def _query_filter(self, *args, **kwargs):
        return SharedCart.objects.filter(*args, **kwargs)