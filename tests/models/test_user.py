from tests import TestCase

from elabodeal.models import User


class TestUserModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(User, 'publisher'), True)
		self.assertEqual(hasattr(User, 'username'), True)
		self.assertEqual(hasattr(User, 'email'), True)
		self.assertEqual(hasattr(User, 'email_verified'), True)
		self.assertEqual(hasattr(User, 'email_verified_at'), True)
		self.assertEqual(hasattr(User, 'is_active'), True)
		self.assertEqual(hasattr(User, 'is_online'), True)
		self.assertEqual(hasattr(User, 'is_staff'), True)
		self.assertEqual(hasattr(User, 'is_superuser'), True)
		self.assertEqual(hasattr(User, 'created_at'), True)
		self.assertEqual(hasattr(User, 'updated_at'), True)


	def test_meta_options(self):
		user = User()

		self.assertEqual(user.USERNAME_FIELD, 'email')
		self.assertEqual(user.REQUIRED_FIELDS, ['username'])

	def test_manager_create_user_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')
			
		self.assertNotEqual(user, None)	

		created_user = User.objects.get(id=user.id)

		self.assertEqual(created_user.email, user.email)
		self.assertEqual(created_user.username, user.username)

	def test_manager_create_superuser_method(self):
		user = User.objects.create_superuser(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		self.assertNotEqual(user, None)

		created_user = User.objects.get(id=user.id)
		
		self.assertEqual(created_user.is_superuser, True)

	def test_manager_update_settings_method(self):
		user = User.objects.create_user(email='xyz@xyz.pl',
										username='xyz',
										password='xyz')

		settings_for_update = {'username': 'zyx'}
	
		updated_user = User.objects.update_settings(user, settings_for_update)

		self.assertEqual(updated_user.username, 'zyx')
		self.assertIsInstance(updated_user, User)

	def test_manager_update_settings_method_if_settings_is_empty(self):
		user = User.objects.create_user(email='xyz@xyz.pl',
										username='xyz',
										password='xyz')

		settings_for_update = {}

		with self.assertRaises(ValueError):
			User.objects.update_settings(user, settings_for_update)

	def test_manager_update_settings_method_if_updated_email(self):
		user = User.objects.create_user(email='xyz@xyz.pl',
										username='xyz',
										password='xyz')
		user.email_verified = True
		user.save()

		settings_for_update = {'email': 'zyx@xyz.pl'}

		updated_user = User.objects.update_settings(user, settings_for_update)

		self.assertEqual(updated_user.email_verified, False)
			