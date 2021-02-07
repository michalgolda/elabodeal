from tests import APITestCase
from django.shortcuts import reverse
from elabodeal.models import User, VerificationCode


class ConfirmEmailEndpointTest(APITestCase):
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

        code = VerificationCode.objects.create_code(
            email='test@test.pl'
        )
        code.save()

        response = self.client.post(
            reverse('api:confirm-email-verification-code'),
            data=dict(
                email='test@test.pl',
                code=code.code
            ),
            format='json'
        )

        self.assertEqual(response.status_code, 200)