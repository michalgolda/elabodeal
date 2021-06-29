from tests import APITestCase
from django.shortcuts import reverse

from elabodeal.models import (
	User,
	Publisher,
	VerificationCode
)


class MeUpdateSettingsEndpoint(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='test@test.pl',
			password='123',
			username='test'
		)

		self.client.login(
			email=self.user.email,
			password='123'
		)

	def test_simple(self):
		response = self.client.put(
			reverse('api:me-update-settings'),
			data={
				'username': 'test1',
				'email': 'test1@test.pl'
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_if_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.put(
			reverse('api:me-update-settings')
		)

		self.assertEqual(response.status_code, 401)


class MeUpdatePublisherSettingsEndpoint(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='xyz@xyz.pl',
			username='xyz',
			password='xyz'
		)

		self.publisher = Publisher.objects.create_publisher(
			first_name='test',
			last_name='test',
			swift='123',
			account_number='123'
		)

		self.user.publisher = self.publisher
		self.user.save()

		self.client.login(
			email=self.user.email,
			password='xyz'
		)

	def test_simple(self):
		response = self.client.put(
			reverse('api:me-publisher-update-settings'),
			data={
				'first_name': 'test1',
				'last_name': 'test1',
				'account_number': '321',
				'swift': '321'
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_if_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.put(
			reverse('api:me-publisher-update-settings')
		)

		self.assertEqual(response.status_code, 401)

	def test_if_user_is_not_publisher(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.put(
			reverse('api:me-publisher-update-settings')
		)

		self.assertEqual(response.status_code, 403)


class MeChangeEmailRequestEndpointTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='test@test.pl',
			password='123',
			username='test'
		)

		self.client.login(
			email=self.user.email,
			password='123'
		)

	def test_simple(self):
		response = self.client.post(
			reverse('api:me-change-email-request'),
			data={
				'email': 'newtest@test.pl',
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_if_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.post(
			reverse('api:me-change-email-request')
		)

		self.assertEqual(response.status_code, 401)


class MeConfirmEmailChangeRequestEndpointTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='test@test.pl',
			password='123',
			username='test'
		)

		self.client.login(
			email=self.user.email,
			password='123'
		)

		self.verification_code = VerificationCode.objects.create_code(
			email='newtest@test.pl'
		)
		self.verification_code.save()

	def test_simple(self):
		response = self.client.post(
			reverse('api:me-confirm-email-change-request'),
			data={
				'email': 'newtest@test.pl',
				'code': self.verification_code.code
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_if_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.post(
			reverse('api:me-confirm-email-change-request')
		)

		self.assertEqual(response.status_code, 401)


class MeChangePasswordEndpointTest(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			email='test@test.pl',
			password='123',
			username='test'
		)

		self.client.login(
			email=self.user.email,
			password='123'
		)

	def test_simple(self):
		response = self.client.put(
			reverse('api:me-change-password'),
			data={
				'new_password': 'New_password123',
				'current_password': '123'
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_if_current_password_is_invalid(self):
		response = self.client.put(
			reverse('api:me-change-password'),
			data={
				'new_password': 'New_password123',
				'current_password': '321'
			}
		)

		self.assertEqual(response.status_code, 400)

	def test_if_user_is_not_authenticated(self):
		self.client.logout()

		response = self.client.put(
			reverse('api:me-change-password')
		)

		self.assertEqual(response.status_code, 401)