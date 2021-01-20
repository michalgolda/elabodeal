from tests import APITestCase
from django.urls import reverse

from elabodeal.models import VerificationCode, User


class TestConfirmEmailVerificationCodeEndpoint(APITestCase):
    def test_simple_response(self):
        user = User.objects.create_user(
            email='xyz@xyz.pl',
            username='xyz',
            password='xyz'
        )
        
        code = VerificationCode.objects.generate(
            user.email
        )
    
        url = reverse(
            'api:confirm-email-verification-code'
        )
        
        data = {
            'email': user.email,
            'code': code.code
        }

        response = self.client.post(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        verified_user = User.objects.filter(id=user.id).first()

        self.assertEqual(verified_user.email_verified, True)

    def test_response_if_code_is_invalid(self):
        user = User.objects.create_user(
            email='xyz@xyz.pl',
            username='xyz',
            password='xyz'
        )
        
        url = reverse(
            'api:confirm-email-verification-code'
        )
        
        data = {
            'email': user.email,
            'code': ''
        }

        response = self.client.post(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 400)
