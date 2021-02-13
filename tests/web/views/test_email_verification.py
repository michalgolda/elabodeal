from tests import WebTestCase
from django.urls import reverse

from elabodeal.models import User


class TestEmailVerificationView(WebTestCase):
	def test_simple(self):
		user = User.objects.create_user(
			email='test@test.pl', 
			username='test', 
			password='johnpassword'
		)

		session = self.client.session
		session['email_for_confirmation'] = user.email
		session.save()

		response = self.client.get(reverse('web:email-verification'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertTemplateUsed(response, 'email_verification.html')
		self.assertIn(user.email.encode('utf-8'), response.content)

	def test_if_email_for_confirmation_is_not_in_session(self):
		response = self.client.get(
			reverse('web:email-verification'),
			follow=True
		)

		self.assertRedirects(
			response, 
			reverse('web:index'), 
			status_code=302,
			target_status_code=200
		)

	def test_if_not_found_user_by_email_for_confirmation(self):
		session = self.client.session
		session['email_for_confirmation'] = 'test@test.pl'
		
		response = self.client.get(
			reverse('web:email-verification'),
			follow=True
		)

		self.assertRedirects(
			response, 
			reverse('web:index'), 
			status_code=302,
			target_status_code=200
		)



