from tests import BaseTestCase
from elabodeal.utils import CartSessionManager


class CartSessionManagerTest(BaseTestCase):
    def setUp(self):
        self.session = {
            'cart': {
                'id': '123',
                'products': [
                    {
                        'id': '1',
                        'price': 2.00,
                        'title': 'test',
                        'author': 'test',
                        'selected': True,
                        'cover_img_path': 'test'
                    }
                ]
            }
        }

    def test_id_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.id, '123')

    def test_product_count_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.product_count, 1)

    def test_products_property(self):
        cart_manager = CartSessionManager(self.session)

        products = cart_manager.products

        self.assertEqual(
            products, 
            [
                CartSessionManager.Product(
                    id='1',
                    price=2.00,
                    title='test',
                    author='test',
                    cover_img_path='test'
                )
            ]
        )

    def test_selected_products(self):
        cart_manager = CartSessionManager(self.session)

        selected_products = cart_manager.selected_products

        self.assertEqual(
            selected_products, 
            [
                CartSessionManager.Product(
                    id='1',
                    price=2.00,
                    title='test',
                    author='test',
                    cover_img_path='test'
                )
            ]
        )

    def test_isEmpty_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.isEmpty, False)

    def test_total_price_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.total_price, '2.00')

    def test_total_price_of_selected_property(self):
        cart_manager = CartSessionManager(self.session)

        total_price = cart_manager.total_price_of_selected_products

        self.assertEqual(total_price, '2.00')

    def test_asdict_property(self):
        cart_manager = CartSessionManager(self.session)

        cart_manager_as_dict = cart_manager.asdict

        self.assertEquals(
            cart_manager_as_dict, 
            {
                'id': '123',
                'isEmpty': False,
                'products': [{
                    'id': '1',
                    'price': 2.00,
                    'title': 'test',
                    'author': 'test',
                    'selected': True,
                    'cover_img_path': 'test'
                }],
                'total_price': '2.00',
                'product_count': 1,
                'total_price_of_selected_products': '2.00'
            }
        )

    def test_get_product_method(self):
        cart_manager = CartSessionManager(self.session)

        product = cart_manager.get_product('1')

        self.assertEqual(
            product, 
            CartSessionManager.Product(
                id='1',
                price=2.00,
                title='test',
                author='test',
                cover_img_path='test'
            )
        )

    def test_product_is_selected_method(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.product_is_selected('1'), True)

    def test_product_in_cart_method(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.product_in_cart('1'), True)

    def test_add_method(self):
        session = {}

        cart_manager = CartSessionManager(session)

        product = CartSessionManager.Product(
            id='1',
            price=2.00,
            title='test',
            author='test',
            cover_img_path='test'
        )

        cart_manager.add(product)

        self.assertEqual(
            cart_manager.products, 
            [
                CartSessionManager.Product(
                    id='1',
                    price=2.00,
                    title='test',
                    author='test',
                    selected=True,
                    cover_img_path='test'
                )
            ]
        )

    def test_remove_method(self):
        cart_manager = CartSessionManager(self.session)

        cart_manager.remove('1')

        self.assertEqual(cart_manager.products, [])

    def test_select_method(self):
        session = {
            'cart': {
                'products': [{
                    'id': '1',
                    'price': 2.00,
                    'title': 'test',
                    'author': 'test',
                    'selected': False,
                    'cover_img_path': 'test'
                }]
            }
        }

        cart_manager = CartSessionManager(session)

        cart_manager.select('1')

        selected_products = cart_manager.selected_products

        self.assertEqual(len(selected_products), 1)

    def test_deselect_method(self):
        cart_manager = CartSessionManager(self.session)

        cart_manager.deselect('1')

        selected_products = cart_manager.selected_products

        self.assertEqual(selected_products, [])

    def test_clear_method(self):
        cart_manager = CartSessionManager(self.session)

        cart_manager.clear()

        self.assertEqual(cart_manager.products, [])

    def test_commit_method(self):
        self.session = {}

        cart_manager = CartSessionManager(self.session)

        product = CartSessionManager.Product(
            id='1',
            price=2.00,
            title='test',
            author='test',
            cover_img_path='test'
        )

        cart_manager.add(product);
        cart_manager.commit()

        updated_session = {
            'cart': cart_manager.asdict
        }

        self.assertEqual(self.session, updated_session)
