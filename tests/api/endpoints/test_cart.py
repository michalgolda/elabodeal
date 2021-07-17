import uuid
from unittest import skip
from tests import APITestCase

from django.shortcuts import reverse


class CartEndpointTest(APITestCase):
	pass


class SaveCartEndpointTest(APITestCase):
	pass


class CheckoutSessionEndpointTest(APITestCase):
	def test_create_checkout_session(self):
		response = self.client.post(reverse('api:checkout-session'))
		response_data = response.json()

		self.assertEqual(response.status_code, 201)

		self.assertIn('id', response_data)
		self.assertIn('step', response_data)

	def test_update_checkout_session(self):
		session = self.client.session
		session['checkout_session'] = dict(
			id=str(uuid.uuid4()),
			step='deliver'
		)
		session.save()

		response = self.client.put(
			reverse('api:checkout-session'),
			data=dict(
				first_name='test',
				last_name='test',
				email='test@test.pl'
			)
		)
		response_data = response.json()

		delivery = dict(
			first_name='test',
			last_name='test',
			email='test@test.pl'
		)

		self.assertEqual(response.status_code, 200)

		self.assertEqual(response_data.get('delivery'), delivery)

	def test_remove_checkout_session(self):
		session = self.client.session
		session['checkout_session'] = None
		session.save()

		response = self.client.delete(reverse('api:checkout-session'))

		self.assertEqual(response.status_code, 200)


class SucceedCheckoutSessionEndpoint(APITestCase):
	pass