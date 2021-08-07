import datetime
from unittest import mock
from tests import BaseTestCase

from django.core import mail
from django.test import override_settings

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

		self.mock_publisher = mock.MagicMock()


class GetProductListInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.get_all_by.return_value = True

		interactor = GetProductListInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(
			self.mock_publisher
		)

		self.mock_product_repo.get_all_by.assert_called_once_with(
			publisher=self.mock_publisher
		)

		self.assertEqual(interactor_returned_value, True)


class GetProductInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.get_one_by.return_value = True

		product_id = 1

		interactor = GetProductInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(
			self.mock_publisher,
			product_id
		)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			publisher=self.mock_publisher,
			id=product_id
		)

		self.assertEqual(interactor_returned_value, True)


class DeleteProductInteractorTest(BaseProductInteractorTest):

	def test_execute(self):
		self.mock_product_repo.delete_by.return_value = True

		product_id = 1

		interactor = DeleteProductInteractor(
			product_repo=self.mock_product_repo
		)
		interactor_returned_value = interactor.execute(
			self.mock_publisher,
			product_id
		)

		self.mock_product_repo.delete_by.assert_called_once_with(
			publisher=self.mock_publisher,
			id=product_id
		)

		self.assertEqual(interactor_returned_value, True)


class CreateProductInteractorTest(BaseProductInteractorTest):

	def setUp(self, *args, **kwargs):
		super().setUp(*args, **kwargs)

		self.mock_user = mock.MagicMock(
			email='test'
		)
		self.mock_file = mock.MagicMock()
		self.mock_product = mock.MagicMock(
			cover_img=mock.MagicMock(
				path='test'
			)
		)
		self.mock_category = mock.MagicMock()
		self.mock_product_group = mock.MagicMock()
		self.mock_product_premiere = mock.MagicMock()
		self.mock_product_language = mock.MagicMock()

		self.mock_product_group_repo.add.return_value = self.mock_product_group
		self.mock_category_repo.get_one_by.return_value = self.mock_category
		self.mock_product_language_repo.get_one_by.return_value = self.mock_product_language

		self.mock_file_repo.add.return_value = self.mock_file

		self.mock_product_premiere_repo.add.return_value = self.mock_product_premiere

		self.mock_product_repo.add.return_value = self.mock_product

		self.mock_interactor_args = {
			'user': self.mock_user,
			'publisher': self.mock_publisher,
			'product_group_id': None,
			'category_id': 1,
			'product_language_id': 1,
			'title': 'test',
			'description': 'test',
			'contents': 'test',
			'author': 'test',
			'isbn': 'test',
			'price': 12.00,
			'age_category': 7,
			'cover_img': self.mock_file,
			'other_images': [self.mock_file],
			'files': [self.mock_file],
			'premiere_datetime': datetime.datetime.now(),
			'copies': 1,
			'page_count': 1,
			'published_year': 1	
		}

		mail.outbox = []

	@override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
	def test_execute(self):
		interactor = CreateProductInteractor(
			file_repo=self.mock_file_repo,
			product_repo=self.mock_product_repo,
			category_repo=self.mock_category_repo,
			product_group_repo=self.mock_product_group_repo,
			product_language_repo=self.mock_product_language_repo,
			product_premiere_repo=self.mock_product_premiere_repo
		)
		created_product = interactor.execute(**self.mock_interactor_args)

		self.mock_product_group_repo.add.assert_called_once_with(
			publisher=self.mock_publisher
		)

		self.mock_category_repo.get_one_by.assert_called_once_with(
			id=self.mock_interactor_args['category_id']
		)

		self.mock_product_language_repo.get_one_by.assert_called_once_with(
			id=self.mock_interactor_args['product_language_id']
		)

		self.mock_file_repo.add.assert_called()

		self.mock_product_premiere_repo.add.assert_called_once_with(
			datetime=self.mock_interactor_args['premiere_datetime']
		)

		self.mock_product_repo.add.assert_called_once_with(
			publisher=self.mock_publisher,
			group=self.mock_product_group,
			category=self.mock_category,
			language=self.mock_product_language,
			age_category=self.mock_interactor_args['age_category'],
			title=self.mock_interactor_args['title'],
			description=self.mock_interactor_args['description'],
			contents=self.mock_interactor_args['contents'],
			author=self.mock_interactor_args['author'],
			isbn=self.mock_interactor_args['isbn'],
			price=self.mock_interactor_args['price'],
			copies=self.mock_interactor_args['copies'],
			published_year=self.mock_interactor_args['published_year'],
			page_count=self.mock_interactor_args['page_count'],
			cover_img=self.mock_interactor_args['cover_img'],
			files=self.mock_interactor_args['files'],
			other_images=self.mock_interactor_args['other_images'],
			premiere=self.mock_product_premiere
		)

		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(created_product, self.mock_product)

	def test_execute_if_product_group_does_not_exists(self):
		self.mock_product_group_repo.get_one_by.return_value = None

		self.mock_interactor_args['product_group_id'] = 1

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				file_repo=self.mock_file_repo,
				product_repo=self.mock_product_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(**self.mock_interactor_args)

	def test_execute_if_category_does_not_exists(self):
		self.mock_category_repo.get_one_by.return_value = None

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				file_repo=self.mock_file_repo,
				product_repo=self.mock_product_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(**self.mock_interactor_args)

	def test_execute_if_product_language_does_not_exists(self):
		self.mock_product_language_repo.get_one_by.return_value = None

		with self.assertRaises(ResourceDoesNotExists):
			interactor = CreateProductInteractor(
				file_repo=self.mock_file_repo,
				product_repo=self.mock_product_repo,
				category_repo=self.mock_category_repo,
				product_group_repo=self.mock_product_group_repo,
				product_language_repo=self.mock_product_language_repo,
				product_premiere_repo=self.mock_product_premiere_repo
			)
			interactor.execute(**self.mock_interactor_args)