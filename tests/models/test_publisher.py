import uuid
from tests.base import TestCase

from elabodeal.models import Publisher


class PublisherModelTest(TestCase):
    
    def test_fields(self):
        self.assertEqual(hasattr(Publisher, 'id'), True)
        self.assertEqual(
            Publisher._meta.get_field('id').primary_key,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('id').default,
            uuid.uuid4
        )
        self.assertEqual(
            Publisher._meta.get_field('id').editable,
            False
        )

        self.assertEqual(hasattr(Publisher, 'first_name'), True)
        self.assertEqual(
            Publisher._meta.get_field('first_name').max_length, 
            Publisher.MAX_FIRST_NAME_LENGTH
        )

        self.assertEqual(hasattr(Publisher, 'last_name'), True)
        self.assertEqual(
            Publisher._meta.get_field('last_name').max_length,
            Publisher.MAX_LAST_NAME_LENGTH
        )

        self.assertEqual(hasattr(Publisher, 'account_number'), True)
        self.assertEqual(
            Publisher._meta.get_field('account_number').max_length,
            Publisher.MAX_ACCOUNT_NUMBER_LENGTH
        )

        self.assertEqual(hasattr(Publisher, 'swift'), True)
        self.assertEqual(
            Publisher._meta.get_field('swift').max_length,
            Publisher.MAX_SWIFT_LENGHT
        )

        self.assertEqual(hasattr(Publisher, 'created_at'), True)
        self.assertEqual(
            Publisher._meta.get_field('created_at').auto_now_add,
            True
        )

        self.assertEqual(hasattr(Publisher, 'updated_at'), True)
        self.assertEqual(
            Publisher._meta.get_field('updated_at').auto_now,
            True
        )

    def test_manager_create_Publisher_method(self):
        created_Publisher = Publisher.objects.create_publisher(
            first_name='Test',
            last_name='Test',
            account_number='123',
            swift='123'
        )

        self.assertEqual(created_Publisher.first_name, 'Test')
        self.assertEqual(created_Publisher.last_name, 'Test')
        self.assertEqual(created_Publisher.account_number, '123')
        self.assertEqual(created_Publisher.swift, '123')
