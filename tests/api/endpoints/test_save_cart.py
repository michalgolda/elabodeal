from tests import APITestCase
from django.shortcuts import reverse
from elabodeal.models import User


class SaveCartEndpointTest(APITestCase):
    def test_simple(self):
        User.objects.create_user(
            email='test@test.pl',
            username='test',
            password='test'
        )

        self.client.login(
            email='test@test.pl',
            password='test'
        )

        session = self.client.session
        session['cart'] = dict(items=[])
        session.save()

        response = self.client.post(
            reverse('api:save-cart'),
            data=dict(
                title='test',
                description='test'
            ),
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_authenticated(self):
        response = self.client.post(reverse('api:save-cart'))

        self.assertEqual(response.status_code, 401)