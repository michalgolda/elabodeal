import uuid
from tests.base import BaseTestCase

from elabodeal.models import File


class FileModelTest(BaseTestCase):
	
	def test_fields(self):
		self.assertEqual(hasattr(File, 'id'), True)
		self.assertEqual(
			File._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			File._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			File._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(File, 'size'), True)
		self.assertEqual(hasattr(File, 'path'), True)

		self.assertEqual(hasattr(File, 'extension'), True)
		self.assertEqual(
			File._meta.get_field('extension').max_length,
			File.MAX_EXTENSION_LENGTH
		)
		self.assertEqual(
			File._meta.get_field('extension').choices,
			File.Extension.choices
		)

		self.assertEqual(hasattr(File, 'type'), True)
		self.assertEqual(
			File._meta.get_field('type').max_length,
			File.MAX_TYPE_LENGTH
		)
		self.assertEqual(
			File._meta.get_field('type').choices,
			File.Type.choices
		)

		self.assertEqual(hasattr(File, 'hash'), True)
		self.assertEqual(
			File._meta.get_field('hash').max_length,
			File.MAX_HASH_LENGTH
		)

		self.assertEqual(hasattr(File, 'uploaded_at'), True)
		self.assertEqual(
			File._meta.get_field('uploaded_at').auto_now_add,
			True
		)
