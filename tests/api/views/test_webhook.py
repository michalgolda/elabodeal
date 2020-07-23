from django.urls import reverse
from tests.base import APITestCase


class TestWebHookAPIView(APITestCase):
	def test_check_stripe_signature(self):
		response = self.client.post(reverse('api:webhooks'), {
				'HTTP_STRIPE_SIGNATURE': '123'
			})

		self.assertEqual(response.status_code, 403)

	def test_if_not_stripe_signature(self):
		response = self.client.post(reverse('api:webhooks'))

		self.assertEqual(response.status_code, 403)