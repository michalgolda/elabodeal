from tests.base import BaseTestCase

from elabodeal.models import Publisher


class TestPublisherModel(BaseTestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create_publisher(
            first_name='test',
            last_name='test',
            account_number='123',
            country='PL',
            swift='123'
        ) 
    
    def test_fields(self):
        self.assertEqual(hasattr(Publisher, 'first_name'), True)
        self.assertEqual(hasattr(Publisher, 'last_name'), True)
        self.assertEqual(hasattr(Publisher, 'account_number'), True)
        self.assertEqual(hasattr(Publisher, 'country'), True)
        self.assertEqual(hasattr(Publisher, 'swift'), True)
        self.assertEqual(hasattr(Publisher, 'sell_notification'), True)

    def test_manager_create_publisher_method(self):
        self.assertIsInstance(self.publisher, Publisher)

    def test_manager_update_settings_method(self):
        options = {
            'first_name': 'test123'
        }

        updated_publisher = Publisher.objects.update_settings(self.publisher, options)

        self.assertIsInstance(self.publisher, Publisher)
        self.assertEqual(updated_publisher.first_name, 'test123')