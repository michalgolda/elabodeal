from tests.base import BaseTestCase

from elabodeal.models import User


class TestUserModel(BaseTestCase):
	def test_fields(self):
		self.assertEqual(hasattr(User, 'first_name'), True)
		self.assertEqual(hasattr(User, 'last_name'), True)
		self.assertEqual(hasattr(User, 'username'), True)
		self.assertEqual(hasattr(User, 'email'), True)
		self.assertEqual(hasattr(User, 'email_verified'), True)
		self.assertEqual(hasattr(User, 'email_verified_at'), True)
		self.assertEqual(hasattr(User, 'is_staff'), True)
		self.assertEqual(hasattr(User, 'is_superuser'), True)
		self.assertEqual(hasattr(User, 'is_active'), True)
		self.assertEqual(hasattr(User, 'created_at'), True)
		self.assertEqual(hasattr(User, 'updated_at'), True)

	def test_meta_options(self):
		user = User()

		self.assertEqual(user.USERNAME_FIELD, 'email')
		self.assertEqual(user.REQUIRED_FIELDS, ['username'])