import uuid
from tests.base import BaseTestCase

from elabodeal.models import Publisher


class PublisherModelTest(BaseTestCase):
    
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

        self.assertEqual(hasattr(Publisher, 'banner_text'), True)
        self.assertEqual(
            Publisher._meta.get_field('banner_text').max_length,
            Publisher.MAX_BANNER_TEXT_LENGTH
        )
        self.assertEqual(
            Publisher._meta.get_field('banner_text').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('banner_text').default,
            None
        )

        self.assertEqual(hasattr(Publisher, 'banner_product'), True)
        self.assertEqual(
            Publisher._meta.get_field('banner_product').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('banner_product').default,
            None
        )

        self.assertEqual(hasattr(Publisher, 'avatar_img'), True)
        self.assertEqual(
            Publisher._meta.get_field('avatar_img').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('avatar_img').default,
            None
        )

        self.assertEqual(hasattr(Publisher, 'banner_img'), True)
        self.assertEqual(
            Publisher._meta.get_field('banner_img').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('banner_img').default,
            None
        )

        self.assertEqual(hasattr(Publisher, 'who_you_are'), True)
        self.assertEqual(
            Publisher._meta.get_field('who_you_are').max_length,
            Publisher.MAX_WHO_YOU_ARE_LENGTH
        )
        self.assertEqual(
            Publisher._meta.get_field('who_you_are').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('who_you_are').default,
            None
        )

        self.assertEqual(hasattr(Publisher, 'bio'), True)
        self.assertEqual(
            Publisher._meta.get_field('bio').max_length,
            Publisher.MAX_BIO_LENGTH
        )
        self.assertEqual(
            Publisher._meta.get_field('bio').null,
            True
        )
        self.assertEqual(
            Publisher._meta.get_field('bio').default,
            None
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

    # def test_manager_create_Publisher_method(self):
    #     created_Publisher = Publisher.objects.create_publisher(
    #         first_name='Test',
    #         last_name='Test',
    #         account_number='123',
    #         swift='123'
    #     )

    #     self.assertEqual(created_Publisher.first_name, 'Test')
    #     self.assertEqual(created_Publisher.last_name, 'Test')
    #     self.assertEqual(created_Publisher.account_number, '123')
    #     self.assertEqual(created_Publisher.swift, '123')
