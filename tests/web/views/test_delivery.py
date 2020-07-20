from tests.base import WebTestCase
from django.urls import reverse


class TestDeliveryView(WebTestCase):
	def test_simple(self):
		session = self.client.session
		session['cart'] = {'item_count': 1}
		session.save()

		form_data = {
			'email': 'test@test.pl',
			'first_name': 'test',
			'last_name': 'test',
			'gift': False
		}

		response = self.client.post(reverse('web:cart-delivery'), form_data, follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment.html')

	def test_gift_form(self):
		session = self.client.session
		session['cart'] = {'item_count': 1}
		session.save()

		form_data = {
			'email': 'test@test.pl',
			'first_name': 'test',
			'last_name': 'test',
			'gift': True,
			'gift_first_name': 'test',
			'gift_last_name': 'test',
			'gift_email': 'test@test.pl' 
		}

		response = self.client.post(reverse('web:cart-delivery'), form_data, follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment.html')

	def test_main_form_error(self):
		session = self.client.session
		session['cart'] = {'item_count': 1}
		session.save()

		form_data = {
			'email': 'test',
			'first_name': 'test',
			'last_name': 'test',
			'gift': False 
		}

		response = self.client.post(reverse('web:cart-delivery'), form_data)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'delivery.html')
		self.assertFormError(response, 'form', 'email', 'Podaj poprawny email')

	def test_gift_form_error(self):
		session = self.client.session
		session['cart'] = {'item_count': 1}
		session.save()

		form_data = {
			'email': 'test',
			'first_name': 'test',
			'last_name': 'test',
			'gift': True,
			'gift_first_name': 'test',
			'gift_last_name': 'test',
			'gift_email': 'test' 
		}

		response = self.client.post(reverse('web:cart-delivery'), form_data)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'delivery.html')
		self.assertFormError(response, 'form', 'gift_email', 'Podaj poprawny email')

	def test_redirect_if_session_not_contain_cart_object(self):
		response = self.client.get(reverse('web:cart-delivery'), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'cart.html')


