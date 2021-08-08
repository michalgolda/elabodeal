from elabodeal.api.repositories import Repository
from elabodeal.models import PurchasedProduct


class PurchasedProductRepository(Repository):
    def add(self, *args, **kwargs):
        return PurchasedProduct.objects.create(*args, **kwargs)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())

    def save(self, purchased_product):
        purchased_product.save()

        return purchased_product

    def _query_filter(self, *args, **kwargs):
        return PurchasedProduct.objects.filter(*args, **kwargs)