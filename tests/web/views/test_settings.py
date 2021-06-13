from tests import WebTestCase
from django.urls import reverse
from elabodeal.models import User


class TestSettingsView(WebTestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='test@test.pl',
			password='123',
			username='test'
		)

		self.client.login(
			email=self.user.email,
			password='123'
		)

	def test_simple(self):
		response = self.client.get(reverse('web:settings'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'settings.html')

	def test_when_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.get(reverse('web:settings'))

		self.assertRedirects(
            response, 
            reverse('web:login'), 
            status_code=302, 
            target_status_code=200, 
            fetch_redirect_response=True
        )