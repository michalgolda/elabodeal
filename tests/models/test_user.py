from tests.base import TestCase

from elabodeal.models import User


class TestUserModel(TestCase):
	def test_fields(self):
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

		__user = User.objects.filter(id=user.id).first()

		self.assertNotEqual(user, None)	
		self.assertNotEqual(__user, None)
		self.assertEqual(__user.email, user.email)
		self.assertEqual(__user.username, user.username)

	def test_manager_create_user_method_if_email_is_empty(self):
		with self.assertRaises(ValueError):
					user = User.objects.create_user(
						email='',
						username='xyz', 
						password='xyz')

	def test_manager_create_user_method_if_username_is_empty(self):
		with self.assertRaises(ValueError):
					user = User.objects.create_user( 
						email='xyz@xyz.pl', 
						username='',
						password='xyz')

	def test_manager_create_superuser_method(self):
		user = User.objects.create_superuser(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		__user = User.objects.filter(id=user.id).first()
		
		self.assertNotEqual(user, None)
		self.assertNotEqual(__user, None)
		self.assertEqual(__user.is_superuser, True)
		self.assertEqual(__user.email, user.email)
		self.assertEqual(__user.username, user.username)



		

		