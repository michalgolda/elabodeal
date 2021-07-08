from unittest import mock
from tests import BaseTestCase

from elabodeal.api.interactors import (
	AddProductToCartInteractor,
	RemoveProductFromCartInteractor
)


class AddProductToCartInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.utils.CartSessionManager')
	@mock.patch('elabodeal.api.repositories.ProductRepository')
	def setUp(self, mock_cart_manager, mock_product_repo):
		self.mock_cart_manager = mock_cart_manager
		self.mock_product_repo = mock_product_repo

	def test_execute(self):
		mock_product = mock.MagicMock(id=1, price=1)

		self.mock_product_repo.get_one_by.return_value = mock_product

		interactor = AddProductToCartInteractor(
			product_repo=self.mock_product_repo,
			cart_manager=self.mock_cart_manager
		)

		product = interactor.execute(mock_product.id)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			id=mock_product.id
		)

		self.mock_cart_manager.add.assert_called_once_with(
			mock_product.id,
			mock_product.price
		)

		self.mock_cart_manager.commit.assert_called()

		self.assertEqual(product, mock_product)


class RemoveProductFromCartInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.utils.CartSessionManager')
	def setUp(self, mock_cart_manager):
		self.mock_cart_manager = mock_cart_manager

	def test_execute(self):
		interactor = RemoveProductFromCartInteractor(
			cart_manager=self.mock_cart_manager
		)
		interactor.execute(1)

		self.mock_cart_manager.remove.assert_called_once_with(1)
		self.mock_cart_manager.commit.assert_called()


