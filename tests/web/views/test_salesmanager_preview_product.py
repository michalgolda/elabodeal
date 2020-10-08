from django.urls import reverse
from tests.base import WebTestCase
from elabodeal.models import User, Category, Product


class TestSalesManagerPreviewProductView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')
		user.is_seller = True
		user.save()

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

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:salesmanager-preview-product', args=[1]))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/preview_product.html')
		self.assertIn('12.00 zł'.encode('utf-8'), response.content)

	def test_if_product_does_not_exist(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')
		user.is_seller = True
		user.save()


		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(
			reverse('web:salesmanager-preview-product', args=[1]), 
			follow=True
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8'
		)
		self.assertTemplateUsed(response, 'salesmanager/index.html')


	def test_if_user_is_not_logged(self):
		response = self.client.get(
			reverse('web:salesmanager-preview-product', args=[1]),
			follow=True
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertTemplateUsed(response, 'index.html')

	def test_if_user_is_not_seller(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(
			reverse('web:salesmanager-preview-product', args=[1]),
			follow=True
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8'
		)
		self.assertTemplateUsed(response, 'salesmanager/start.html')