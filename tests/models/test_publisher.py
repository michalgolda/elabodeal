from tests.base import BaseTestCase

from elabodeal.models import Publisher


class TestPublisherModel(BaseTestCase):
    def test_fields(self):
        self.assertEqual(hasattr(Publisher, 'user'), True)
        self.assertEqual(hasattr(Publisher, 'first_name'), True)
        self.assertEqual(hasattr(Publisher, 'last_name'), True)
        self.assertEqual(hasattr(Publisher, 'account_number'), True)
        self.assertEqual(hasattr(Publisher, 'country'), True)
        self.assertEqual(hasattr(Publisher, 'swift'), True)
        self.assertEqual(hasattr(Publisher, 'sell_notification'), True)