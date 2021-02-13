from tests import APITestCase

from django.shortcuts import reverse
from django.test import override_settings

from elabodeal.models import User


class ResendConfirmChangeEmailEndpointTest(APITestCase):
    
    @override_settings(task_always_eager=True)
    def test_simple(self):
        User.objects.create_user(
            email='test@test.pl',
            username='test',
            password='test'
        )

        self.client.login(
            email='test',
            password='test'
        )

        response = self.client.post(
            reverse('api:resend-change-email-confirmation'),
            data=dict(
                email='test@test.pl'
            ),
            format='json'
        )

        self.assertEqual(response.status_code, 200)
