from tests import BaseTestCase
from elabodeal.utils import CartSessionManager


class CartSessionManagerTest(BaseTestCase):
    def setUp(self):
        self.session = {
            'cart': {
                'products': [
                    {
                        'id': '1',
                        'price': 2.00
                    }
                ]
            }
        }

    def test_product_count_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.product_count, 1)

    def test_products_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(
            cart_manager.products, 
            [
                CartSessionManager.Product(
                    id='1',
                    price=2.00
                )
            ]
        )

    def test_total_price_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.total_price, '2.00')


    def test_isEmpty_property(self):
        cart_manager = CartSessionManager(self.session)

        self.assertEqual(cart_manager.isEmpty, False)


    def test_add_method(self):
        session = {}

        cart_manager = CartSessionManager(session)

        cart_manager.add(1, 2.00)

        self.assertEqual(
            cart_manager.products, 
            [
                CartSessionManager.Product(
                    id='1',
                    price=2.00
                )
            ]
        )

    def test_remove_method(self):
        cart_manager = CartSessionManager(self.session)

        cart_manager.remove('1')

        self.assertEqual(cart_manager.products, [])

    def test_commit_method(self):
        self.session = {}

        cart_manager = CartSessionManager(self.session)

        cart_manager.add(1, 2.00);

        cart_manager.commit()

        updated_session = {
            'cart': {
                'products': [
                    {
                        'id': '1',
                        'price': 2.00
                    }
                ],
                'total_price': '2.00',
                'product_count': 1,
                'isEmpty': False
            }
        }

        self.assertEqual(self.session, updated_session)
