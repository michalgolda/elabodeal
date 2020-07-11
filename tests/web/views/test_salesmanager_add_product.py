from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import User


class TestSalesManagerAddProductView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@wp.pl', username='test', password='123')
		user.is_seller = True
		user.save()

		self.client.login(email='test@wp.pl', password='123')

		response = self.client.get(reverse('web:salesmanager-add-product'))

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/add_product.html')

	def test_when_user_is_not_seller(self):
		user = User.objects.create_user(email='test@wp.pl', username='test', password='123')

		self.client.login(email='test@wp.pl', password='123')

		response = self.client.get(reverse('web:salesmanager-add-product'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'salesmanager/start.html')

	def test_when_user_is_not_authenticated(self):
		response = self.client.get(reverse('web:salesmanager-add-product'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')