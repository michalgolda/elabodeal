from tests.base import WebTestCase
from django.urls import reverse


class TestDeliveryView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:cart-delivery'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'delivery.html')
		self.assertIn('Dostawa'.encode('utf-8'), response.content)