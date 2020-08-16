from django.urls import reverse
from tests.base import APITestCase

from elabodeal.models import Product, User, Category, SharedCart


class TestShareCartsAPIView(APITestCase):
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
			isbn=123,
			url_name='test'
		)

		product.save()

		session = self.client.session
		session['cart'] = {'products': [{'id': product.id}]}
		session.save()

		response = self.client.post(reverse('api:share-carts'), {'title': 'test', 'description': 'test'})

		self.assertEqual(response.status_code, 201)
		self.assertIsNot(response.data.get('shared_cart_code'), None)
		self.assertEqual(len(response.data['shared_cart_code']), 10)

		shared_cart = SharedCart.objects.filter(code=response.data['shared_cart_code']).first()

		self.assertNotEqual(shared_cart, None)