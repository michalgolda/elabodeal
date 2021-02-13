from unittest import mock
from tests import BaseTestCase

from django.test import override_settings
from django.core import mail

from elabodeal.api.interactors import ResendConfirmEmailInteractor
from elabodeal.api.exceptions import ErrorRegistry


class ResendConfirmEmailInteractorTest(BaseTestCase):
    
    @mock.patch('elabodeal.api.repositories.UserRepository')
    @mock.patch('elabodeal.api.repositories.VerificationCodeRepository')
    def setUp(self, mock_user_repo, mock_code_repo):
        self.mock_user_repo = mock_user_repo
        self.mock_code_repo = mock_code_repo

        mail.outbox = []

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        task_always_eager=True
    )
    def test_execute(self):
        self.mock_user_repo.find_by_email.return_value = True
        self.mock_code_repo.find_by_email.return_value = None
        
        with ResendConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(email='test@test.pl')

        self.assertEqual( self.mock_code_repo.save.called, True )
        self.assertEqual(len(mail.outbox), 1)

    def test_execute_if_user_does_not_exist(self):
        self.mock_user_repo.find_by_email.return_value = None

        with self.assertRaises(ErrorRegistry.RESEND_CONFIRM_EMAIL):
            with ResendConfirmEmailInteractor(
                user_repo=self.mock_user_repo,
                code_repo=self.mock_code_repo
            ) as interactor:
                interactor.execute(email='test')

    @override_settings(task_always_eager=True)
    def test_execute_remove_existing_code(self):
        self.mock_user_repo.find_by_email.return_value = True
        self.mock_code_repo.find_by_email.return_value = True

        with ResendConfirmEmailInteractor(
            user_repo=self.mock_user_repo,
            code_repo=self.mock_code_repo
        ) as interactor:
            interactor.execute(email='test')

        self.assertEqual(self.mock_code_repo.delete.called, True)
