from unittest import mock

from tests import BaseTestCase

from elabodeal.api.interactors import UpdateUserSettingsInteractor
from elabodeal.api.exceptions import ErrorRegistry


class UpdateUserSettingsInteractorTest(BaseTestCase):
    
    @mock.patch('elabodeal.api.repositories.UserRepository')
    def setUp(self, mock_user_repo):
        self.mock_user_repo = mock_user_repo

    def test_execute(self):
        user = mock.MagicMock(username='test')

        with UpdateUserSettingsInteractor(
            user_repo=self.mock_user_repo
        ) as interactor:
            interactor.execute(
                user=user, 
                options=dict(
                    username='asd'
                )
            )

        self.assertEqual(user.username, 'asd')
        self.assertEqual(self.mock_user_repo.save.called, True)