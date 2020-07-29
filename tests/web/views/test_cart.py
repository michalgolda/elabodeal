from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import Product, User, Category


class TestCartView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:cart'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'cart.html')
		self.assertIn('Twój koszyk jest pusty'.encode('utf-8'), response.content)

	def test_redirect_if_product_does_exist_in_cart(self):
		session = self.client.session
		session['cart'] = {'products': [{'id': 1}]}
		session.save()

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
			isbn=123,
			url_name='test'
		)

		product.save()

		form_data = {
			'action_type': 'add-product',
			'product_id': 1
		}

		response = self.client.post(reverse('web:cart'), form_data)
		
		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 302)
