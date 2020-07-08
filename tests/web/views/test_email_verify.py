from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import User

class TestEmailVerifyView(WebTestCase):
	def test_simple(self):
		User.objects.create_user(email='test@test.pl', username='test', password='johnpassword')
		self.client.login(email='test@test.pl', password='johnpassword')

		session = self.client.session
		session['email'] = 'test@test.pl'
		session.save()

		response = self.client.get(reverse('web:account-email-verify'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'email_verify.html')
		self.assertIn('test@test.pl'.encode('utf-8'), response.content)