from elabodeal.api.repositories import Repository
from elabodeal.models import Product


class ProductRepository(Repository):
    def get(self, id: int) -> Product:
        return Product.objects.filter(id=id).first()

    def delete(self, product: Product) -> None:
        product.delete()

    def save(self, product: Product) -> Product:
        product.save()

        return product