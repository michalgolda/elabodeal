
from tests.base import TestCase

from django.core import mail
from django.conf import settings

from elabodeal.models import BannedUser, User


class TestBannedUserModel(TestCase):
	def test_fields(self):
		self.assertEqual(hasattr(BannedUser,'user'), True)
		self.assertEqual(hasattr(BannedUser,'reason'), True)
		self.assertEqual(hasattr(BannedUser,'banned_at'), True)

	def test_manager_ban_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		banned_user = BannedUser.objects.ban(user_id=user.id, reason='xyz')

		__banned_user = BannedUser.objects.filter(id=banned_user.user.id).first()

		self.assertNotEqual(banned_user, None)
		self.assertNotEqual(__banned_user, None)
		self.assertEqual(__banned_user.reason, banned_user.reason)

	def test_manager_ban_method_if_user_does_not_exists(self):
		with self.assertRaises(BannedUser.DoesNotExist):
			banned_user = BannedUser.objects.ban(user_id=0, reason='xyz')

	def test_manager_ban_method_send_email(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		settings.EMAIL_HOST_USER = 'abc@abc.pl'

		banned_user = BannedUser.objects.ban(user_id=user.id, reason='xyz')

		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].subject, 'Elabodeal - Blokada konta')

	def test_manager_unban_method(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		banned_user = BannedUser.objects.ban(user_id=user.id, reason='xyz')

		unbanned_user = BannedUser.objects.unban(user_id=banned_user.user.id)
		
		__banned_user = BannedUser.objects.filter(user__id=banned_user.user.id).first()

		self.assertNotEqual(unbanned_user, None)
		self.assertEqual(__banned_user, None)

	def test_manager_unban_method_if_user_does_not_exists(self):
		with self.assertRaises(BannedUser.DoesNotExist):
			banned_user = BannedUser.objects.unban(user_id=0)

	def test_manager_unban_method_send_email(self):
		user = User.objects.create_user(
			email='xyz@xyz.pl', 
			username='xyz', 
			password='xyz')

		banned_user = BannedUser(user=user, reason='xyz')
		banned_user.save()

		settings.EMAIL_HOST_USER = 'abc@abc.pl'

		BannedUser.objects.unban(user_id=banned_user.id)

		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].subject, 'Elabodeal - Odblokowano konto')
		self.assertIn(banned_user.user.email, mail.outbox[0].body)


		