from tests.base import BaseTestCase

from elabodeal.models import ProductOpinion


class TestProductOpinionModel(BaseTestCase):
    def test_fields(self):
        self.assertEqual(hasattr(ProductOpinion, 'user'), True)
        self.assertEqual(hasattr(ProductOpinion, 'content'), True)
        self.assertEqual(hasattr(ProductOpinion, 'created_at'), True)
        self.assertEqual(hasattr(ProductOpinion, 'updated_at'), True)