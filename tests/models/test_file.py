from tests.base import BaseTestCase

from elabodeal.models import File


class TestFileModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(File, 'size'), True)
		self.assertEqual(hasattr(File, 'name'), True)
		self.assertEqual(hasattr(File, 'extension'), True)
		self.assertEqual(hasattr(File, 'mime'), True)
		self.assertEqual(hasattr(File, 'uploaded_at'), True)
		self.assertEqual(hasattr(File, 'url'), True)
