from tests import APITestCase
from django.urls import reverse

from elabodeal.models import VerificationCode, User


class TestConfirmEmailVerificationCodeEndpoint(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='xyz@xyz.pl',
            username='xyz',
            password='xyz'
        )
        
        self.code = VerificationCode.objects.generate(
            self.user.email
        )

    def test_simple_request(self):
        url = reverse(
            'api:confirm-email-verification-code'
        )
        data = {
            'email': self.user.email,
            'code': self.code.code
        }

        response = self.client.post(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        verified_user = User.objects.filter(id=self.user.id).first()

        self.assertEqual(verified_user.email_verified, True)