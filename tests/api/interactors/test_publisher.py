from unittest import mock
from tests import BaseTestCase
from elabodeal.api.interactors import CreatePublisherInteractor


class CreatePublisherInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.UserRepository')
    @mock.patch('elabodeal.api.repositories.PublisherRepository')
    def setUp(self, mock_user_repo, mock_publisher_repo):
        self.mock_user_repo = mock_user_repo
        self.mock_publisher_repo = mock_publisher_repo

        self.mock_user = mock.MagicMock()
        self.mock_publisher = mock.MagicMock()

        self.mock_publisher_repo.add.return_value = self.mock_publisher

    def test_execute(self):
        interactor = CreatePublisherInteractor(
            user_repo=self.mock_user_repo,
            publisher_repo=self.mock_publisher_repo
        )
        created_publisher = interactor.execute(
            user=self.mock_user,
            swift='123',
            first_name='test',
            last_name='test',
            account_number='123'
        ) 

        self.mock_publisher_repo.add.assert_called_once_with(
            swift='123',
            first_name='test',
            last_name='test',
            account_number='123'
        )

        self.mock_user_repo.save.assert_called_once_with(self.mock_user)

        self.assertEqual(created_publisher, self.mock_publisher)
        self.assertEqual(self.mock_user.publisher, self.mock_publisher)
