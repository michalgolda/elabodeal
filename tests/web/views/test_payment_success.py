from django.urls import reverse
from tests.base import WebTestCase


class PaymentSuccessView(WebTestCase):
	def get(self, request):
		session = self.client.session
		session['delivery'] = {}
		session.save()

		response = self.client.get(reverse('web:payment-success'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment_success.html')