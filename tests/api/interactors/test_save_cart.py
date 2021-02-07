from tests import BaseTestCase
from unittest import mock

from elabodeal.api.interactors import SaveCartInteractor
from elabodeal.api.exceptions import ErrorRegistry


class SaveCartInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.CartRepository')
    @mock.patch('elabodeal.api.repositories.ProductRepository')
    def setUp(self, mock_cart_repo, mock_product_repo):
        self.mock_cart_repo = mock_cart_repo
        self.mock_product_repo = mock_product_repo

    def test_execute(self):
        mock_cart_session = mock.MagicMock(items=[])

        with SaveCartInteractor(
            cart_repo=self.mock_cart_repo,
            product_repo=self.mock_product_repo
        ) as interactor:
            interactor.execute(
                title='test',
                description='test',
                cart_session=mock_cart_session,
                user=None
            )

        self.assertEquals(self.mock_cart_repo.save.called, True)

    def test_execute_if_cart_session_is_empty(self):
        with self.assertRaises(ErrorRegistry.SAVE_CART):
            with SaveCartInteractor(
                cart_repo=self.mock_cart_repo,
                product_repo=self.mock_product_repo
            ) as interactor:
                interactor.execute(
                    title='test',
                    description='test',
                    cart_session=None,
                    user=None
                )