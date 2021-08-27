import uuid
from dataclasses import dataclass, asdict
    

class CartSessionManager:

    @dataclass
    class Product:
        id: str
        title: str
        author: str
        price: float
        cover_img_path: str
        selected: bool = True

    def __init__(self, session):
        self.session = session

        self._products = []
        self._id = None

        cart = self.session.get('cart')

        if not cart: return
        
        self._id = cart.get('id')

        cart_products = cart.get('products')

        for cart_product in cart_products:
            cart_product_id = cart_product['id']
            cart_product_title = cart_product['title']
            cart_product_price = cart_product['price']
            cart_product_author = cart_product['author']
            cart_product_selected = cart_product['selected']
            cart_product_cover_img_path = cart_product['cover_img_path']

            product = self.Product(
                id=cart_product_id,
                title=cart_product_title,
                price=cart_product_price,
                author=cart_product_author,
                selected=cart_product_selected,
                cover_img_path=cart_product_cover_img_path
            )

            self._products.append(product)

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
    
    def get_product(self, product_id):
        for product in self._products:
            if product.id == product_id:
                return product

        return None

    def product_is_selected(self, product_id):
        product = self.get_product(product_id)

        if not product: return

        product_selected = product.selected

        return product_selected

    def product_in_cart(self, product_id):
        return True if self.get_product(product_id) else False

    def add(self, product):
        product_in_cart = self.product_in_cart(product.id)

        if product_in_cart: return

        self._products.append(product)

    def remove(self, product_id):
        self._products = list(
            filter(
                lambda product: product.id != product_id,
                self._products
            )
        )


    def select(self, product_id):
        product = self.get_product(product_id)

        if not product: return

        product.selected = True

    def deselect(self, product_id):
        product = self.get_product(product_id)

        if not product: return

        product.selected = False

    def clear(self):
        self._products = []

    def commit(self):
        cart_id = str(uuid.uuid4())

        self.session['cart'] = self.asdict
        self.session['cart']['id'] = cart_id

        self._id = cart_id
