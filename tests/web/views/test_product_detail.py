from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import Product, Category, User

class TestProductDetailView(WebTestCase):
	def test_simple(self):
		user = User.objects.create(email='test@wp.pl', username='test', password='123')
		
		category = Category(
			name='test'
		)

		category.save()

		product = Product(
			author='Test',
			user=user,
			category=category,
			title='test',
			description='test',
			price=12,
			page_count=123,
			isbn=123
		)

		product.save()

		response = self.client.get(reverse('web:product-detail', args=[1]),)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'product_detail.html')
		self.assertIn('test'.encode('utf-8'), response.content)
