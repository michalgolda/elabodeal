from tests import APITestCase
from django.urls import reverse
from elabodeal.models import User


class UpdateUserSettingsEndpointTest(APITestCase):
    def test_simple(self):
        user = User.objects.create_user(
            email='test@test.pl',
            username='test',
            password='test'
        )

        self.client.login(
            email='test@test.pl',
            password='test'
        )
        
        response = self.client.put(
            reverse('api:update-user-settings'),
            data=dict(
                username=user.username,
                email=user.email
            ),
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_authenticated(self):
        response = self.client.put(
            reverse('api:update-user-settings')
        )

        self.assertEqual(response.status_code, 401)