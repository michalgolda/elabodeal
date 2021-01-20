from tests import WebTestCase
from django.urls import reverse

from elabodeal.models import User


class TestUserSettingsView(WebTestCase):
    def setUp(self):
        self.url = url = reverse('web:user-settings')

    def test_simple_response(self):
        user = User.objects.create_user(
            email='xyz@xyz.pl',
            username='xyz',
            password='xyz'
        )

        self.client.login(
            email=user.email, 
            password='xyz'
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-settings.html')

    def test_response_if_user_is_not_logged(self):
        response = self.client.get(self.url)

        self.assertRedirects(
            response, 
            reverse('web:login'), 
            status_code=302, 
            target_status_code=200, 
            fetch_redirect_response=True
        )