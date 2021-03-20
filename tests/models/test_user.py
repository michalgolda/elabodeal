import uuid
from tests import TestCase

from elabodeal.models import User


class UserModelTest(TestCase):
	
	def test_fields(self):
		self.assertEqual(hasattr(User, 'id'), True)
		self.assertEqual(
			User._meta.get_field('id').primary_key,
			True
		)
		self.assertEqual(
			User._meta.get_field('id').default,
			uuid.uuid4
		)
		self.assertEqual(
			User._meta.get_field('id').editable,
			False
		)

		self.assertEqual(hasattr(User, 'publisher'), True)
		self.assertEqual(
			User._meta.get_field('publisher').null,
			True
		)
		self.assertEqual(
			User._meta.get_field('publisher').blank,
			True
		)

		self.assertEqual(hasattr(User, 'username'), True)
		self.assertEqual(
			User._meta.get_field('username').max_length,
			User.MAX_USERNAME_LENGTH
		)

		self.assertEqual(hasattr(User, 'email'), True)
		self.assertEqual(
			User._meta.get_field('email').unique,
			True
		)

		self.assertEqual(hasattr(User, 'email_verified'), True)
		self.assertEqual(
			User._meta.get_field('email_verified').default,
			False
		)

		self.assertEqual(hasattr(User, 'email_verified_at'), True)
		self.assertEqual(
			User._meta.get_field('email_verified_at').null,
			True
		)
		self.assertEqual(
			User._meta.get_field('email_verified_at').blank,
			True
		)

		self.assertEqual(hasattr(User, 'is_staff'), True)
		self.assertEqual(
			User._meta.get_field('is_staff').default,
			False
		)

		self.assertEqual(hasattr(User, 'is_online'), True)
		self.assertEqual(
			User._meta.get_field('is_online').default,
			False
		)

		self.assertEqual(hasattr(User, 'is_superuser'), True)
		self.assertEqual(
			User._meta.get_field('is_superuser').default,
			False
		)

		self.assertEqual(hasattr(User, 'created_at'), True)
		self.assertEqual(
			User._meta.get_field('created_at').auto_now_add,
			True
		)

		self.assertEqual(hasattr(User, 'updated_at'), True)
		self.assertEqual(
			User._meta.get_field('updated_at').auto_now,
			True
		)


	def test_options(self):
		self.assertEqual(User.USERNAME_FIELD, 'email')
		self.assertEqual(User.REQUIRED_FIELDS, ['username'])

		self.assertEqual(User._meta.db_table, 'users')

	def test_has_perm_method(self):
		user = User()

		self.assertEqual(user.has_perm('perm'), False)
		self.assertEqual(user.has_module_perms('elabodeal'), False)

	def test_manager_create_superuser_method(self):
		created_user = User.objects.create_superuser(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz'
		)

		self.assertNotEqual(created_user, None)
		self.assertEqual(created_user.email, 'xyz@xyz.pl')
		self.assertEqual(created_user.username, 'xyz')
		self.assertEqual(created_user.is_superuser, True)
		self.assertEqual(created_user.is_staff, True)
		self.assertEqual(created_user.email_verified, True)

	def test_manager_create_user_method(self):
		created_user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz'
		)
			
		self.assertNotEqual(created_user, None)	
		self.assertEqual(created_user.email, 'xyz@xyz.pl')
		self.assertEqual(created_user.username, 'xyz')
		self.assertEqual(created_user.is_superuser, False)
		self.assertEqual(created_user.is_staff, False)