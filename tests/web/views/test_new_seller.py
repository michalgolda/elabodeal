from tests.base import WebTestCase
from django.urls import reverse


class TestNewSellerView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:start-selling'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')