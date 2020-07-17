from tests.base import WebTestCase
from django.urls import reverse


class TestPaymentView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:cart-payment'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment.html')