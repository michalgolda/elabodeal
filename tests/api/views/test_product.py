from django.urls import reverse
from tests.base import APITestCase

from elabodeal.models import Product, User, Category


class TestProductUpdateAPIView(APITestCase):
	def test_simple(self):
		user = User.objects.create_user(
			email='test@wp.pl', 
			username='test', 
			password='123'
		)

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

		self.client.login(email='test@wp.pl', password='123')

		response = self.client.put(
			reverse(
				'api:product-update', 
				args=[1]
			), 
			{
				'title': 'asdf', 
				'author': 'asdf'
			}
		)

		self.assertEqual(response.status_code, 200)

		updated_product = Product.objects.filter(id=1).first()

		self.assertEqual(getattr(updated_product, 'author', None), 'asdf')
		self.assertEqual(getattr(updated_product, 'title', None), 'asdf')

