from tests import APITestCase
from django.shortcuts import reverse
from elabodeal.models import User, Cart


class ShareCartEndpoint(APITestCase):
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

        cart = Cart(
            user=user,
            title='test',
            description='test'
        )
        cart.save()

        response = self.client.post(
            reverse(
                'api:share-cart', 
                args=[cart.id]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_authenticated(self):
        response = self.client.post(
            reverse(
                'api:share-cart',
                args=[1]
            )
        )

        self.assertEqual(response.status_code, 401)