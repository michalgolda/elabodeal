from django.urls import reverse
from tests.base import WebTestCase

from elabodeal.models import User, Product, Category, PurchasedProduct


class TestPurchasedProductDetailView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')

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
			isbn=123,
			url_name='test'
		)

		product.save()

		purchased_product = PurchasedProduct(
			user=user,
			product=product
		)
		purchased_product.save()

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:purchased-product-detail', args=[product.id]))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'purchased_product_detail.html')


	def test_not_found_error(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')
		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:purchased-product-detail', args=[1]), follow=True)
		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'my_books.html')

