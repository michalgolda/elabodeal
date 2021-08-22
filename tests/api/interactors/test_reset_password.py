from unittest import mock
from tests import BaseTestCase

from django.core import mail
from django.test import override_settings

from elabodeal.api.interactors import (
    EndResetPasswordFlowInteractor,
    StartResetPasswordFlowInteractor
)


class StartResetPasswordFlowTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_verification_code_repo):
        self.mock_verification_code_repo = mock_verification_code_repo

        self.mock_verification_code = mock.MagicMock(
            code=123123
        )

        self.mock_verification_code_repo.add.return_value = self.mock_verification_code

        mail.outbox = []

    @override_settings(
        task_always_eager=True,
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    )
    def test_execute(self):
        interactor = StartResetPasswordFlowInteractor(
            verification_code_repo=self.mock_verification_code_repo
        )
        interactor.execute(email='test@test.pl')

        self.mock_verification_code_repo.add.assert_called_once_with(
            email='test@test.pl'
        )

        self.assertEqual(len(mail.outbox), 1)


class EndResetPasswordFlowInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.UserRepository')
    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_user_repo, mock_verification_code_repo):
        self.mock_user_repo = mock_user_repo
        self.mock_verification_code_repo = mock_verification_code_repo

        self.mock_user = mock.MagicMock(
            email='test@test.pl',
            set_password=mock.MagicMock()
        )

        self.mock_user_repo.get_one_by.return_value = self.mock_user

    def test_execute(self):
        interactor = EndResetPasswordFlowInteractor(
            user_repo=self.mock_user_repo,
            verification_code_repo=self.mock_verification_code_repo
        )
        interactor.execute(
            email=self.mock_user.email,
            password='123'
        )

        self.mock_user_repo.get_one_by.assert_called_once_with(
            email=self.mock_user.email
        )

        self.mock_user.set_password.assert_called_once_with('123')

        self.mock_user_repo.save.assert_called_once_with(self.mock_user)

        self.mock_verification_code_repo.delete_by.assert_called_once_with(
            email=self.mock_user.email
        )