from tests import TestCase

from django.http import JsonResponse
from django.shortcuts import reverse

from elabodeal.models import User


class TestUserSettingsView(TestCase):
    def test_simple_response(self):
        user = User.objects.create_user(email='xyz@xyz.pl',
                                        username='xyz',
                                        password='xyz')

        self.client.login(email=user.email, password='xyz')
        
        response = self.client.get(reverse('web:user-settings'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-settings.html')

    def test_response_if_user_is_not_logged(self):
        response = self.client.get(reverse('web:user-settings'))

        self.assertRedirects(response, 
                             reverse('web:login'), 
                             status_code=302, 
                             target_status_code=200, 
                             fetch_redirect_response=True)


class TestUserSaveSettingsAjaxView(TestCase):
    def test_simple_response(self):
        user = User.objects.create_user(email='xyz@xyz.pl',
                                        username='xyz',
                                        password='xyz')

        self.client.login(email=user.email, password='xyz')

        response = self.client.post(reverse('web:user-settings-save'),
                                    data={'username': 'zyx'})

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)

    def test_response_if_user_is_not_logged(self):
        user = User.objects.create_user(email='xyz@xyz.pl',
                                        username='xyz',
                                        password='xyz')

        response = self.client.post(reverse('web:user-settings-save'),
                                    data={'username': 'zyx'})

        self.assertEqual(response.status_code, 401)
        self.assertIsInstance(response, JsonResponse)
        
 
