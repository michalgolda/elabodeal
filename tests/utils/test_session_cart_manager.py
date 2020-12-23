from django.http.request import HttpRequest

from tests import BaseTestCase

from elabodeal.utils import SessionCartManager


class TestSessionCartManager(BaseTestCase):
    def test_init(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}]
            }
        }

        cart = SessionCartManager(request)

        self.assertEquals(cart.items, 
                          [cart.Item(id=1, price=31),
                           cart.Item(id=2, price=21)])

    def test_converting_items_to_dict(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}],
                'total_price': '52.00',
                'item_count': 2
            }
        }

        cart = SessionCartManager(request)

        self.assertEquals(cart.to_dict(), request.session['cart'])

    def test_total_price_param(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}]
            }
        }

        cart = SessionCartManager(request)

        self.assertEqual(cart.total_price, '52.00')

    def test_item_count_param(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}]
            }
        }

        cart = SessionCartManager(request)

        self.assertEqual(cart.item_count, 2)

    def test_add_item_method(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}]
            }
        }

        cart = SessionCartManager(request)

        cart_item = cart.Item(id=3, price=10)
        cart.add_item(cart_item)

        self.assertEqual(cart.item_count, 3)

    def test_remove_item_method(self):
        request = HttpRequest()
        request.session = {
            'cart': {
                'items': [
                    {'id': 1, 'price': 31},
                    {'id': 2, 'price': 21}]
            }
        }

        cart = SessionCartManager(request)

        cart.remove_item(1)

        self.assertEqual(cart.item_count, 1)