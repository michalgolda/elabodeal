from unittest import mock
from tests import BaseTestCase

from elabodeal.api.interactors import (
    SaveCartInteractor,
    ShareSavedCartInteractor,
    DeleteSavedCartInteractor
)


class SaveCartInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.utils.CartSessionManager')
    @mock.patch('elabodeal.api.repositories.CartRepository')
    @mock.patch('elabodeal.api.repositories.ProductRepository')
    def setUp(self, mock_cart_manager, mock_cart_repo, mock_product_repo):
        self.mock_cart_repo = mock_cart_repo
        self.mock_product_repo = mock_product_repo
        self.mock_cart_manager = mock_cart_manager

        self.mock_user = mock.MagicMock()
        self.mock_cart = mock.MagicMock()
        self.mock_product = mock.MagicMock(id=1)

        self.mock_cart_repo.add.return_value = self.mock_cart

        type(self.mock_cart_manager).products = mock.PropertyMock(
            return_value=[self.mock_product]
        )

        self.mock_product_repo.get_one_by.return_value = self.mock_product

    def test_execute(self):
        interactor = SaveCartInteractor(
            cart_repo=self.mock_cart_repo,
            product_repo=self.mock_product_repo,
            cart_manager=self.mock_cart_manager
        )
        interactor.execute(
            user=self.mock_user,
            title='test',
            description='test'
        )

        self.mock_cart_repo.add.assert_called_once_with(
            user=self.mock_user,
            title='test',
            description='test'
        )

        self.mock_product_repo.get_one_by.assert_called_once_with(
            id=self.mock_product.id
        )

        self.mock_cart.products.add.assert_called_once_with(self.mock_product)

        self.mock_cart_repo.save.assert_called_once_with(self.mock_cart)


class ShareSavedCartInteractorTest(BaseTestCase):
    
    @mock.patch('elabodeal.api.repositories.CartRepository')
    @mock.patch('elabodeal.api.repositories.SharedCartRepository')
    def setUp(self, mock_cart_repo, mock_shared_cart_repo):
        self.mock_cart_repo = mock_cart_repo
        self.mock_shared_cart_repo = mock_shared_cart_repo

        self.mock_cart = mock.MagicMock(id=1)
        self.mock_shared_cart = mock.MagicMock()

        self.mock_cart_repo.get_one_by.return_value = self.mock_cart

        self.mock_shared_cart_repo.add.return_value = self.mock_shared_cart

    def test_execute(self):
        interactor = ShareSavedCartInteractor(
            cart_repo=self.mock_cart_repo,
            shared_cart_repo=self.mock_shared_cart_repo
        )
        shared_cart = interactor.execute(cart_id=self.mock_cart.id)

        self.mock_cart_repo.get_one_by.assert_called_once_with(
            id=self.mock_cart.id
        )

        self.mock_shared_cart_repo.add.assert_called_once_with(self.mock_cart)

        self.assertEqual(shared_cart, self.mock_shared_cart)   


class DeleteSavedCartInteractorTest(BaseTestCase):

    @mock.patch('elabodeal.api.repositories.CartRepository')
    def setUp(self, mock_cart_repo):
        self.mock_cart_repo = mock_cart_repo

        self.mock_user = mock.MagicMock()
        
        self.mock_cart_repo.delete_by.return_value = True

    def test_execute(self):
        interactor = DeleteSavedCartInteractor(
            cart_repo=self.mock_cart_repo
        )
        deleted_product = interactor.execute(
            user=self.mock_user,
            cart_id=1
        )

        self.mock_cart_repo.delete_by.assert_called_once_with(
            user=self.mock_user,
            id=1
        )

        self.assertEqual(deleted_product, True)