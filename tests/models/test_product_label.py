from tests.base import BaseTestCase

from elabodeal.models import ProductLabel


class TestProductLabel(BaseTestCase):
    def test_fields(self):
        self.assertEqual(hasattr(ProductLabel, 'name'), True)
        self.assertEqual(hasattr(ProductLabel, 'color'), True) 
        