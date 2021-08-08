from unittest import mock

from django.core import mail
from django.test import override_settings

from tests import BaseTestCase

from elabodeal.api.interactors import (
    UserRegisterConfirmationInteractor,
    ResendUserRegisterConfirmationInteractor
)


class UserRegisterConfirmationInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.UserRepository')
    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_user_repo, mock_verification_code_repo):
        self.mock_user_repo = mock_user_repo
        self.mock_verification_code_repo = mock_verification_code_repo

        self.mock_user = mock.MagicMock(
            email_verified=False,
            email_verified_at=None
        )
        
        self.mock_user_repo.get_one_by.return_value = self.mock_user

    def test_execute(self):
        code = 123123
        email = 'test@test.pl'

        interactor = UserRegisterConfirmationInteractor(
            user_repo=self.mock_user_repo,
            verification_code_repo=self.mock_verification_code_repo
        )
        interactor.execute(
            code=code,
            email=email
        )

        self.mock_user_repo.get_one_by.assert_called_once_with(
            email=email
        )

        self.mock_user_repo.save.assert_called_once_with(self.mock_user)

        self.mock_verification_code_repo.delete_by.assert_called_once_with(
            email=email
        )

        self.assertEqual(self.mock_user.email_verified, True)


class ResendUserRegisterConfirmationInteractorTest(BaseTestCase):
    
    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_verification_code_repo):
        self.mock_verification_code_repo = mock_verification_code_repo

        self.mock_verification_code = mock.MagicMock(
            code=123123
        )

        self.mock_verification_code_repo.add.return_value = self.mock_verification_code_repo

        mail.outbox = []

    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_execute(self):
        interactor = ResendUserRegisterConfirmationInteractor(
            verification_code_repo=self.mock_verification_code_repo
        )
        interactor.execute(
            email='test@test.pl'
        )

        self.mock_verification_code_repo.delete_by.assert_called_once_with(
            email='test@test.pl'
        )

        self.assertEqual(len(mail.outbox), 1)