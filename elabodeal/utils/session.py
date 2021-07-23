import uuid
from dataclasses import dataclass, asdict
    

class CartSessionManager:

    @dataclass
    class Product:
        id: str
        price: float
        selected: bool

    def __init__(self, session):
        self.session = session
        self._products = []
        self._id = None

        cart = self.session.get('cart')

        if cart:
            self._id = cart.get('id')

            cart_products = cart.get('products')

            for cart_product in cart_products:
                cart_product_id = cart_product['id']
                cart_product_price = cart_product['price']
                cart_product_selected = cart_product['selected']

                self._products.append(
                    self.Product(
                        cart_product_id,
                        cart_product_price,
                        cart_product_selected
                    )
                )

    @property
    def id(self):
        return self._id

    @property
    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return self._products

    @property
    def selected_products(self):
        return list(filter(lambda product: product.selected, self._products))

    @property
    def total_price_of_selected_products(self):
        sum = 0.00

        selected_products = self.selected_products

        for product in selected_products:
            sum += product.price

        return '{0:.2f}'.format(round(sum, 2))

    @property
    def isEmpty(self):
        return len(self._products) == 0

    @property
    def total_price(self):
        sum = 0.00
        for product in self._products:
            sum += product.price

        return '{0:.2f}'.format(round(sum, 2))

    @property
    def asdict(self):
        return dict(
            id=self._id,
            isEmpty=self.isEmpty,
            total_price=self.total_price,
            product_count=self.product_count,
            products=[asdict(p) for p in self._products],
            total_price_of_selected_products=self.total_price_of_selected_products,
        )

    def product_is_selected(self, product_id):
        return bool(
            list(
                filter(
                    lambda product: product.id == product_id,
                    self.selected_products
                )
            )
        )

    def add(self, product_id, product_price, product_selected = True):
        product_in_cart = bool(
            list(
                filter(
                    lambda product: product == product_id,
                    self._products
                )
            )
        )

        if product_in_cart: return

        product = self.Product(
            product_id,
            product_price,
            product_selected
        )

        self._products.append(product)

    def remove(self, product_id):
        self._products = list(
            filter(
                lambda product: product.id != product_id,
                self._products
            )
        )

    def select(self, product_id):
        product = None

        for cart_product in self._products:
            if cart_product.id == product_id:
                product = cart_product

        if not product: return

        product.selected = True

    def deselect(self, product_id):
        product = None

        for cart_product in self._products:
            if cart_product.id == product_id:
                product = cart_product

        if not product: return

        product.selected = False

    def clear(self):
        self._products = []

    def commit(self):
        cart_id = str(uuid.uuid4())

        self.session['cart'] = self.asdict
        self.session['cart']['id'] = cart_id

        self._id = cart_id
