from unittest import mock

from tests import BaseTestCase

from elabodeal.api.interactors import UpdatePublisherSettingsInteractor
from elabodeal.api.exceptions import ErrorRegistry


class UpdatePublisherSettingsInteractorTest(BaseTestCase):
    
    @mock.patch('elabodeal.api.repositories.PublisherRepository')
    def setUp(self, mock_publisher_repo):
        self.mock_publisher_repo = mock_publisher_repo

    def test_execute(self):
        publisher = mock.MagicMock(first_name='test')
        user = mock.MagicMock(publisher=publisher)

        with UpdatePublisherSettingsInteractor(
            publisher_repo=self.mock_publisher_repo
        ) as interactor:
            interactor.execute(
                user=user, 
                options=dict(
                    first_name='asd'
                )
            )

        self.assertEqual(publisher.first_name, 'asd')
        self.assertEqual(self.mock_publisher_repo.save.called, True)

    def test_execute_if_user_are_not_publisher(self):
        user = mock.MagicMock(
            publisher=None
        )

        with self.assertRaises(ErrorRegistry.UPDATE_PUBLISHER_SETTINGS):
            with UpdatePublisherSettingsInteractor(
                publisher_repo=self.mock_publisher_repo
            ) as interactor:
                interactor.execute(user=user, options=None)