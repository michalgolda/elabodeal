from django.urls import reverse
from tests.base import WebTestCase

from elabodeal.models import User


class TestMyBooksView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(email='test@wp.pl', username='test', password='123')
		self.client.login(email='test@wp.pl', password='123')

		response = self.client.get(reverse('web:my-books'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'my_books.html')

	def test_if_user_not_authenticated(self):
		response = self.client.get(reverse('web:my-books'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')
