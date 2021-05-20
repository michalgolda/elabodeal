import datetime
from unittest import mock
from tests import BaseTestCase

from elabodeal.api.interactors import (
	GetProductInteractor,
	GetProductListInteractor,
	DeleteProductInteractor,
	CreateProductInteractor
)
from elabodeal.api.exceptions import ResourceDoesNotExists


class BaseProductInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.FileRepository')
	@mock.patch('elabodeal.api.repositories.ProductRepository')
	@mock.patch('elabodeal.api.repositories.CategoryRepository')
	@mock.patch('elabodeal.api.repositories.ProductGroupRepository')
	@mock.patch('elabodeal.api.repositories.ProductLanguageRepository')
	@mock.patch('elabodeal.api.repositories.ProductPremiereRepository')
	def setUp(
		self, mock_file_repo, mock_product_repo, 
		mock_category_repo, mock_product_group_repo, 
		mock_product_language_repo, mock_product_premiere_repo
	):
		self.mock_file_repo = mock_file_repo
		self.mock_product_repo = mock_product_repo
		self.mock_category_repo = mock_category_repo
		self.mock_product_group_repo = mock_product_group_repo
		self.mock_product_language_repo = mock_product_language_repo
		self.mock_product_premiere_repo = mock_product_premiere_repo


class GetProductListInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.get_all_by.return_value = True

		mock_publisher = mock.MagicMock()

		interactor = GetProductListInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(mock_publisher)

		self.mock_product_repo.get_all_by.assert_called_once_with(
			publisher=mock_publisher
		)

		self.assertEqual(interactor_returned_value, True)


class GetProductInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.get_one_by.return_value = True

		mock_publisher = mock.MagicMock()
		product_id = 1

		interactor = GetProductInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(
			mock_publisher,
			product_id
		)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			publisher=mock_publisher,
			id=product_id
		)

		self.assertEqual(interactor_returned_value, True)


class DeleteProductInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.delete_by.return_value = True

		mock_publisher = mock.MagicMock()
		product_id = 1

		interactor = DeleteProductInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(
			mock_publisher,
			product_id
		)

		self.mock_product_repo.delete_by.assert_called_once_with(
			publisher=mock_publisher,
			id=product_id
		)

		self.assertEqual(interactor_returned_value, True)


class CreateProductInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.add.return_value = True
		self.mock_file_repo.add.return_value = True
		self.mock_product_group_repo.add.return_value = True
		self.mock_category_repo.get_one_by.return_value = True
		self.mock_product_language_repo.get_one_by.return_value = True
		self.mock_product_premiere_repo.add.return_value = True

		mock_publisher = mock.MagicMock()
		mock_cover_img = mock.MagicMock()
		product_group_id = None
		category_id = 1
		product_language_id = 1
		title = 'test'
		description = 'test'
		contents = 'test'
		author = 'test'
		isbn = 'test'
		price = 12.00
		copies = 200
		page_count = 100
		age_category = 7
		other_images, files = [True], [True]
		premiere_datetime = datetime.datetime.now()

		interactor = CreateProductInteractor(
			product_repo=self.mock_product_repo,
			file_repo=self.mock_file_repo,
			category_repo=self.mock_category_repo,
			product_group_repo=self.mock_product_group_repo,
			product_language_repo=self.mock_product_language_repo,
			product_premiere_repo=self.mock_product_premiere_repo
		)
		interactor_returned_value = interactor.execute(
			publisher=mock_publisher,
			product_group_id=product_group_id,
			category_id=category_id,
			product_language_id=product_language_id,
			title=title,
			description=description,
			contents=contents,
			author=author,
			isbn=isbn,
			price=price,
			copies=copies,
			page_count=page_count,
			age_category=age_category,
			cover_img=mock_cover_img,
			other_images=other_images,
			files=files,
			premiere_datetime=premiere_datetime
		)

		self.mock_product_group_repo.add.assert_called_once_with(
			publisher=mock_publisher
		)

		self.mock_category_repo.get_one_by.assert_called_once_with(
			id=category_id
		)

		self.mock_product_language_repo.get_one_by.assert_called_once_with(
			id=product_language_id
		)

		self.mock_product_premiere_repo.add.assert_called_once_with(
			datetime=premiere_datetime
		)

		self.mock_product_repo.add.assert_called_once_with(
			publisher=mock_publisher,
			group=True,
			category=category_id,
			language=product_language_id,
			age_category=age_category,
			title=title,
			description=description,
			contents=contents,
			author=author,
			isbn=isbn,
			price=price,
			copies=copies,
			page_count=page_count,
			cover_img=True,
			files=[True],
			other_images=[True],
			premiere=True
		)

		self.assertEqual(interactor_returned_value, True)

	def test_execute_if_product_group_does_not_exists(self):
		self.mock_product_group_repo.get_one_by.return_value = False

		mock_publisher = mock.MagicMock()
		mock_cover_img = mock.MagicMock()
		product_group_id = 1
		category_id = 1
		product_language_id = 1
		title = 'test'
		description = 'test'
		contents = 'test'
		author = 'test'
		isbn = 'test'
		price = 12.00
		copies = 200
		page_count = 100
		age_category = 7
		other_images, files = [True], [True]
		premiere_datetime = None

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				product_repo=self.mock_product_repo,
				file_repo=self.mock_file_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(
				publisher=mock_publisher,
				product_group_id=product_group_id,
				category_id=category_id,
				product_language_id=product_language_id,
				title=title,
				description=description,
				contents=contents,
				author=author,
				isbn=isbn,
				price=price,
				copies=200,
				page_count=100,
				age_category=age_category,
				cover_img=mock_cover_img,
				other_images=other_images,
				files=files,
				premiere_datetime=premiere_datetime
			)

	def test_execute_if_category_does_not_exists(self):
		self.mock_product_group_repo.get_one_by.return_value = True
		self.mock_category_repo.get_one_by.return_value = False

		mock_publisher = mock.MagicMock()
		mock_cover_img = mock.MagicMock()
		product_group_id = 1
		category_id = 1
		product_language_id = 1
		title = 'test'
		description = 'test'
		contents = 'test'
		author = 'test'
		isbn = 'test'
		price = 12.00
		copies = 200
		page_count = 100
		age_category = 7
		other_images, files = [True], [True]
		premiere_datetime = None

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				product_repo=self.mock_product_repo,
				file_repo=self.mock_file_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(
				publisher=mock_publisher,
				product_group_id=product_group_id,
				category_id=category_id,
				product_language_id=product_language_id,
				title=title,
				description=description,
				contents=contents,
				author=author,
				isbn=isbn,
				price=price,
				copies = copies,
				page_count = page_count,
				age_category=age_category,
				cover_img=mock_cover_img,
				other_images=other_images,
				files=files,
				premiere_datetime=premiere_datetime
			)

	def test_execute_if_product_language_does_not_exists(self):
		self.mock_product_group_repo.get_one_by.return_value = True
		self.mock_category_repo.get_one_by.return_value = True
		self.mock_product_language_repo.get_one_by.return_value = False

		mock_publisher = mock.MagicMock()
		mock_cover_img = mock.MagicMock()
		product_group_id = 1
		category_id = 1
		product_language_id = 1
		title = 'test'
		description = 'test'
		contents = 'test'
		author = 'test'
		isbn = 'test'
		price = 12.00
		copies = 200
		page_count = 100
		age_category = 7
		other_images, files = [True], [True]
		premiere_datetime = None

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				product_repo=self.mock_product_repo,
				file_repo=self.mock_file_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(
				publisher=mock_publisher,
				product_group_id=product_group_id,
				category_id=category_id,
				product_language_id=product_language_id,
				title=title,
				description=description,
				contents=contents,
				author=author,
				isbn=isbn,
				price=price,
				copies = copies,
				page_count = page_count,
				age_category=age_category,
				cover_img=mock_cover_img,
				other_images=other_images,
				files=files,
				premiere_datetime=premiere_datetime
			)