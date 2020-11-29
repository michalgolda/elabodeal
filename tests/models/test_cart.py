from unittest import mock

from tests.base import TestCase

from elabodeal.models import (
	Cart, CartItem, Product, 
	User, SharedCart)


class TestCartModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(Cart, 'user'), True)
		self.assertEqual(hasattr(Cart, 'items'), True)
		self.assertEqual(hasattr(Cart, 'title'), True)
		self.assertEqual(hasattr(Cart, 'description'), True)
		self.assertEqual(hasattr(Cart, 'created_at'), True)
		self.assertEqual(hasattr(Cart, 'updated_at'), True)

	def test_manager_share_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl',
			username='xyz',
			password='xyz')
		
		cart = Cart.objects.create(
			user=user,
			title='xyz',
			description='xyz')
		cart.items.set([])
		cart.save()

		shared_cart = Cart.objects.share(cart_id=cart.id)
		
		__shared_cart = SharedCart.objects.filter(id=shared_cart.id).first()

		self.assertNotEqual(__shared_cart, None)
		self.assertEqual(isinstance(shared_cart, SharedCart), True)
