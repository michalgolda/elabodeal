from tests import APITestCase
from django.urls import reverse
from elabodeal.models import Publisher, User


class UpdatePublisherSettingsEndpointTest(APITestCase):
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
        
        publisher = Publisher.objects.create_publisher(
            first_name='xyz',
            last_name='test',
            account_number='123',
            country='PL',
            swift='123'
        )
        
        user.publisher = publisher
        user.save()

        response = self.client.put(
            reverse('api:update-publisher-settings'), 
            data=dict(
                first_name=publisher.first_name,
                last_name=publisher.last_name,
                account_number=publisher.account_number,
                swift=publisher.swift,
                sell_notification=publisher.sell_notification
            ),
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_authenticated(self):
        response = self.client.put(
            reverse('api:update-publisher-settings')
        )

        self.assertEqual(response.status_code, 401)
