from tests import APITestCase
from django.urls import reverse

from elabodeal.models import User


class TestUpdateUserSettingsEndpoint(APITestCase):
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

        url = reverse(
            'api:update-user-settings'
        )

        data = {
            'username': 'test',
            'email': user.email
        }

        response = self.client.put(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        updated_user = User.objects.filter(id=user.id).first()

        self.assertEqual(updated_user.username, 'test')