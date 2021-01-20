from tests import APITestCase
from django.urls import reverse

from elabodeal.models import Publisher, User


class TestUpdatePublisherSettingsEndpoint(APITestCase):
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
        
        publisher = Publisher.objects.create_publisher(
            first_name='xyz',
            last_name='test',
            account_number='123',
            country='PL',
            swift='123'
        )
        
        user.publisher = publisher
        user.save()
    
        url = reverse(
            'api:update-publisher-settings'
        )

        data = {
            'first_name': 'test',
            'last_name': publisher.last_name,
            'account_number': publisher.account_number,
            'swift': publisher.swift,
            'sell_notification': publisher.sell_notification
        }

        response = self.client.put(
            url, 
            data, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        updated_publisher = Publisher.objects.filter(id=publisher.id).first()

        self.assertEqual(updated_publisher.first_name, 'test')