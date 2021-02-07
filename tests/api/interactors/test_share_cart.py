from tests import BaseTestCase
from unittest import mock

from elabodeal.api.interactors import ShareCartInteractor


class ShareCartInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.SharedCartRepository')
    @mock.patch('elabodeal.api.repositories.CartRepository')
    def setUp(self, mock_shared_cart_repo, mock_cart_repo):
        self.mock_shared_cart_repo = mock_shared_cart_repo
        self.mock_cart_repo = mock_cart_repo

    def test_execute(self):
        self.mock_cart_repo.get.return_value = None

        with ShareCartInteractor(
            shared_cart_repo=self.mock_shared_cart_repo,
            cart_repo=self.mock_cart_repo
        ) as interactor:
            interactor.execute(cart_id=1)

        self.assertEqual(self.mock_cart_repo.get.called, True)
        self.assertEqual(self.mock_shared_cart_repo.save.called, True)