from unittest import skip

from tests import WebTestCase

from django.urls import reverse
from django.http import JsonResponse

from elabodeal.models import User, VerificationCode


class TestEmailVerificationView(WebTestCase):
	@skip('This functionality must be refactored')
	def test_simple(self):
		# User.objects.create_user(email='test@test.pl', username='test', password='johnpassword')
		# self.client.login(email='test@test.pl', password='johnpassword')

		# session = self.client.session
		# session['email'] = 'test@test.pl'
		# session.save()

		# response = self.client.get(reverse('web:account-email-verify'))

		# self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'email_verify.html')
		# self.assertIn('test@test.pl'.encode('utf-8'), response.content)
		pass


class TestEmailVerificationAjaxVieW(WebTestCase):
	def test_simple_request(self):	
		user = User.objects.create_user(email='xyz@xyz.pl',
										username='xyz',
										password='xyz')
		
		verify_code = VerificationCode.objects.generate(email=user.email)

		request_data = {}
		request_data['email'] = verify_code.email
		request_data['code'] = verify_code.code

		request_url = reverse('web:verify-email')

		response = self.client.post(request_url, request_data)

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(response, JsonResponse)

	def test_request_if_data_is_none(self):
		request_data = {}
		request_url = reverse('web:verify-email')

		response = self.client.post(request_url, request_data)

		self.assertEqual(response.status_code, 400)
		self.assertIsInstance(response, JsonResponse)


class TestResendEmailVerificationAjaxView(WebTestCase):
	def test_simple_request(self):
		user = User.objects.create_user(email='xyz@xyz.pl',
										username='xyz',
										password='xyz')
		
		request_data = {}
		request_data['email'] = user.email

		request_url = reverse('web:resend-email-verification-code')

		response = self.client.post(request_url, request_data)

		print(response.json())

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(response, JsonResponse)

	def test_request_if_data_is_none(self):
		request_data = {}
		request_url = reverse('web:resend-email-verification-code')

		response = self.client.post(request_url, request_data)

		self.assertEqual(response.status_code, 400)
		self.assertIsInstance(response, JsonResponse)