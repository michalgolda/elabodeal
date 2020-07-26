from django.urls import reverse
from tests.base import WebTestCase

from elabodeal.models import User, Cart, CartItem, Product, Category


class TestSavedCartDetailView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@wp.pl', username='test', password='123')
		
		category = Category(
			name='test'
		)

		category.save()

		product = Product(
			author='test',
			user=user,
			category=category,
			title='test',
			description='test',
			price=12,
			page_count=123,
			isbn=123
		)

		product.save()

		cart = Cart.objects.create(user=user, title='test', description='test')
		cart.save()

		cart_item = CartItem.objects.create(cart=cart, product=product)
		cart_item.save()

		self.client.login(email='test@wp.pl', password='123')

		response = self.client.get(reverse('web:saved-cart-detail', args=[cart.id]))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'saved_cart_detail.html')
		self.assertIn('test'.encode('utf-8'), response.content)
