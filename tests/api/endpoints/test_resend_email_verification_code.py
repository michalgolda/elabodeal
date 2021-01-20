from tests import APITestCase
from django.urls import reverse

from elabodeal.models import User


class TestResendEmailVerificationCodeEndpoint(APITestCase):   
    def test_simple_response(self):
        user = User.objects.create_user(
            email='zyx@zyx.pl',
            username='xyz',
            password='xyz'
        )

        url = reverse(
            'api:resend-email-verification-code'
        )
        data = {
            'email': user.email
        }

        response = self.client.post(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_response_if_email_is_empty(self):
        url = reverse(
            'api:resend-email-verification-code'
        )
        
        data = {
            'email': ''
        }

        response = self.client.post(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 400)
        