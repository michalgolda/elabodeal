from datetime import timedelta

from unittest import mock
from django.utils import timezone
from tests import BaseTestCase

from elabodeal.api.interactors import ConfirmEmailInteractor
from elabodeal.api.exceptions import ErrorRegistry


class ConfirmEmailInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.UserRepository')
    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_user_repo, mock_code_repo):
        self.mock_user_repo = mock_code_repo
        self.mock_code_repo = mock_code_repo

    def test_execute(self):
        user = mock.MagicMock(
            email_verified=None,
            email_verified_at=None
        )

        code = mock.MagicMock(
            code=123,
            expiration_at=timezone.now() + timedelta(seconds=86400)
        )

        self.mock_user_repo.find_by_email.return_value = user
        self.mock_code_repo.find_by_email.return_value = code

        with ConfirmEmailInteractor(
            user_repo=self.mock_user_repo,
            code_repo=self.mock_code_repo
        ) as interactor:
            interactor.execute(
                code=123,
                email='test'
            )

        self.assertEqual(self.mock_code_repo.delete.called, True)
        self.assertEqual(self.mock_user_repo.save.called, True)

    def test_execute_if_user_does_not_exist(self):
        self.mock_user_repo.find_by_email.return_value = None

        with self.assertRaises(ErrorRegistry.CONFIRM_EMAIL):
            with ConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(
                    email='test',
                    code=123
                )

    def test_execute_if_code_does_not_exist(self):
        self.mock_user_repo.find_by_email.return_value = True
        self.mock_code_repo.find_by_email.return_value = None
        
        with self.assertRaises(ErrorRegistry.CONFIRM_EMAIL):
            with ConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(
                    email='test',
                    code=123
                )

    def test_execute_if_code_is_invalid(self):
        self.mock_user_repo.find_by_email.return_value = True
        
        code = mock.MagicMock(code=321)
        
        self.mock_code_repo.find_by_email.return_value = code

        with self.assertRaises(ErrorRegistry.CONFIRM_EMAIL):
            with ConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(
                    email='test',
                    code=123
                )


    def test_execute_if_code_is_invalid(self):
        self.mock_user_repo.find_by_email.return_value = True
        
        code = mock.MagicMock(
            code=123,
            expiration_at=timezone.now() - timedelta(seconds=86400)
        )
        
        self.mock_code_repo.find_by_email.return_value = code
        
        with self.assertRaises(ErrorRegistry.CONFIRM_EMAIL):
            with ConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(
                    email='test',
                    code=123
                )
