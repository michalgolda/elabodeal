from tests import BaseTestCase
from unittest import mock

from django.test import override_settings
from django.core import mail

from elabodeal.api.interactors import (
	UpdateUserSettingsInteractor,
	UpdatePublisherSettingsInteractor,
	ChangeEmailRequestInteractor,
	ConfirmEmailChangeRequestInteractor
)


class UpdateUserSettingsInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.UserRepository')
	def setUp(self, mock_user_repo):
		self.mock_user_repo = mock_user_repo

	def test_execute(self):
		mock_user = mock.MagicMock(
			username='test'
		)

		settings_for_change = {}
		settings_for_change['username'] = 'updated value'

		interactor = UpdateUserSettingsInteractor(
			user_repo=self.mock_user_repo
		)	
		interactor.execute(mock_user, settings_for_change)

		self.mock_user_repo.save.assert_called()

		self.assertEqual(
			mock_user.username, 
			settings_for_change.get('username')
		)


class UpdatePublisherSettingsInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	def setUp(self, mock_publisher_repo):
		self.mock_publisher_repo = mock_publisher_repo

	def test_execute(self):
		mock_publisher = mock.MagicMock(
			first_name='test',
			last_name='test',
			account_number='123',
			swift='123'
		)

		settings_for_change = {}
		settings_for_change['first_name'] = 'updated value'
		settings_for_change['last_name'] = 'updated value'
		settings_for_change['account_number'] = '321'
		settings_for_change['swift'] = '321'

		interactor = UpdatePublisherSettingsInteractor(
			publisher_repo=self.mock_publisher_repo
		)	
		interactor.execute(mock_publisher, settings_for_change)

		self.mock_publisher_repo.save.assert_called()

		self.assertEqual(
			mock_publisher.first_name, 
			settings_for_change.get('first_name')
		)
		self.assertEqual(
			mock_publisher.last_name, 
			settings_for_change.get('last_name')
		)
		self.assertEqual(
			mock_publisher.account_number, 
			settings_for_change.get('account_number')
		)
		self.assertEqual(
			mock_publisher.swift,
			settings_for_change.get('swift')
		)


class ChangeEmailRequestInteractorTest(BaseTestCase):
	
	@mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
	def setUp(self, mock_verification_code_repo):
		self.mock_verification_code_repo = mock_verification_code_repo

	@override_settings(
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        task_always_eager=True
	)
	def test_execute(self):
		self.mock_verification_code_repo.add.return_value = mock.MagicMock(
			email='test@test.pl',
			code='123'
		)

		interactor = ChangeEmailRequestInteractor(
			verification_code_repo=self.mock_verification_code_repo
		)
		interactor.execute(email='test@test.pl')

		self.mock_verification_code_repo.add.assert_called_once_with(
			email='test@test.pl'
		)

		self.assertEqual(len(mail.outbox), 1)


class ConfirmEmailChangeRequestInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.UserRepository')
	@mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
	def setUp(self, mock_user_repo, mock_verification_code_repo):
		self.mock_user_repo = mock_user_repo
		self.mock_verification_code_repo = mock_verification_code_repo

	def test_execute(self):
		mock_user = mock.MagicMock(email=None)

		interactor = ConfirmEmailChangeRequestInteractor(
			user_repo=self.mock_user_repo,
			verification_code_repo=self.mock_verification_code_repo
		)
		interactor.execute(
			user=mock_user,
			email='test@test.pl'
		)

		self.mock_user_repo.save.assert_called_once_with(mock_user)
		
		self.mock_verification_code_repo.delete_by.assert_called_once_with(
			email='test@test.pl'		)


