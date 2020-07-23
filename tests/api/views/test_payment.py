from django.urls import reverse
from tests.base import APITestCase


class TestPaymentAPIView(APITestCase):
	def test_simple_error(self):
		response = self.client.post(reverse('api:payments'))

		self.assertEqual(response.status_code, 400)