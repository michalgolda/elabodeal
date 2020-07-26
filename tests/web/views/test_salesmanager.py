from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import User, Category, Product


class TestSalesManagerView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')
		user.is_seller = True
		user.save()

		category = Category()
		category.name = 'Test'
		category.save()

		product = Product()
		product.category = category
		product.author = 'Test'
		product.user = user
		product.title = 'Test e-book'
		product.description = 'test'
		product.price = 12
		product.page_count = 123
		product.isbn = 123
		product.save()

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:salesmanager'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/index.html')
		self.assertIn('Test e-book'.encode('utf-8'), response.content)

	def test_when_user_is_not_has_products(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')
		user.is_seller = True
		user.save()

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:salesmanager'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/index.html')
		self.assertIn('Nie posiadasz żadnego opublikowanego e-booka zmień to jak najszybciej'.encode('utf-8'), response.content)

	def test_when_user_is_not_seller(self):
		user = User.objects.create_user(email='test@test.pl', username='test', password='123')

		self.client.login(email='test@test.pl', password='123')

		response = self.client.get(reverse('web:salesmanager'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/start.html')

	def test_when_user_is_not_authenticated(self):
		response = self.client.get(reverse('web:salesmanager'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')