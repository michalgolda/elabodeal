from dataclasses import dataclass, asdict
    

class CartSessionManager:

    @dataclass
    class Product:
        id: str
        price: float

    def __init__(self, session):
        self.session = session

        self._products = self._load()

    @property
    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return self._products

    @property
    def total_price(self):
        sum = 0.00
        for product in self._products:
            sum += product.price

        return '{0:.2f}'.format(round(sum, 2))

    def add(self, id, price):
        product = self.Product(str(id), float(price))

        self._products.append(product)

    def remove(self, id):
        updated_state = []

        for product in self._products:
            if product.id != id:
                updated_state.append(product)

        self._products = updated_state

    def commit(self):
        self.session['cart'] = {
            'products': [asdict(p) for p in self._products],
            'total_price': self.total_price,
            'product_count': self.product_count
        }

    def _load(self):
        cart = self.session.get('cart')

        if not cart: return []

        cart_products = cart.get('products')

        return [self.Product(p['id'], float(p['price'])) for p in cart_products]