from unittest import mock
from tests import BaseTestCase

from elabodeal.api.interactors import (
	GetProductGroupInteractor,
	GetProductGroupListInteractor,
	CreateProductGroupInteractor,
	DeleteProductGroupInteractor
)
from elabodeal.api.exceptions import ResourceIsAlreadyExists


class BaseProductGroupInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.ProductGroupRepository')
	def setUp(self, mock_product_group_repo):
		self.mock_product_group_repo = mock_product_group_repo


class GetProductGroupListInteractorTest(BaseProductGroupInteractorTest):
	
	def test_execute(self):
		self.mock_product_group_repo.get_all_by.return_value = True

		mock_publisher = mock.MagicMock()

		interactor = GetProductGroupListInteractor(
			product_group_repo=self.mock_product_group_repo
		)
		interactor_returned_value = interactor.execute(mock_publisher)

		self.mock_product_group_repo.get_all_by.assert_called_once_with(
			publisher=mock_publisher
		)

		self.assertEqual(interactor_returned_value, True)


class GetProductGroupInteractorTest(BaseProductGroupInteractorTest):

	def test_execute(self):
		self.mock_product_group_repo.get_one_by.return_value = True

		mock_publisher = mock.MagicMock()
		product_group_id = 1

		interactor = GetProductGroupInteractor(
			product_group_repo=self.mock_product_group_repo
		)
		interactor_returned_value = interactor.execute(
			mock_publisher,
			product_group_id
		)

		self.mock_product_group_repo.get_one_by.assert_called_once_with(
			publisher=mock_publisher, 
			id=product_group_id
		)
		self.assertEqual(interactor_returned_value, True)


class CreateProductGroupInteractorTest(BaseProductGroupInteractorTest):

	def test_execute(self):
		self.mock_product_group_repo.add.return_value = True

		mock_publisher = mock.MagicMock()

		interactor = CreateProductGroupInteractor(
			product_group_repo=self.mock_product_group_repo
		)
		interactor_returned_value = interactor.execute(mock_publisher)

		self.mock_product_group_repo.add.assert_called_once_with(publisher=mock_publisher)

		self.assertEqual(interactor_returned_value, True)


class DeleteProductGroupInteractorTest(BaseProductGroupInteractorTest):

	def test_execute(self):
		self.mock_product_group_repo.delete_by.return_value = True

		mock_publisher = mock.MagicMock()
		product_group_id = 1

		interactor = DeleteProductGroupInteractor(
			product_group_repo=self.mock_product_group_repo
		)
		interactor_returned_value = interactor.execute(
			mock_publisher,
			product_group_id
		)

		self.mock_product_group_repo.delete_by.assert_called_once_with(
			publisher=mock_publisher,
			id=product_group_id
		)

		self.assertEqual(interactor_returned_value, True)