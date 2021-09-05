from unittest import mock
from tests import BaseTestCase
from elabodeal.api.interactors import (
	CreatePublisherInteractor,
	FollowPublisherInteractor,
	UnFollowPublisherInteractor,
	UpdatePublisherProfileInteractor,
	UpdatePublisherProfileBannerImgInteractor,
	UpdatePublisherProfileAvatarImgInteractor
)


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


class FollowPublisherInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.UserRepository')
	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	def setUp(self, mock_user_repo, mock_publisher_repo):
		self.mock_user_repo = mock_user_repo
		self.mock_publisher_repo = mock_publisher_repo

		self.mock_user = mock.MagicMock(
			followers=mock.MagicMock(
				add=mock.MagicMock()
			),
			already_following=mock.MagicMock(
				return_value=False
			)
		)

		self.mock_publisher = mock.MagicMock(
			id=123,
			followers=mock.MagicMock(
				add=mock.MagicMock()
			)
		)

		self.mock_publisher_repo.get_one_by.return_value = self.mock_publisher

	def test_execute(self):
		interactor = FollowPublisherInteractor(
			user_repo=self.mock_user_repo,
			publisher_repo=self.mock_publisher_repo
		)
		interactor.execute(
			self.mock_user,
			self.mock_publisher.id
		)

		self.mock_user.already_following.assert_called_once_with(
			self.mock_publisher.id
		)

		self.mock_publisher_repo.get_one_by.assert_called_once_with(
			id=self.mock_publisher.id
		)

		self.mock_user.followers.add.assert_called_once_with(self.mock_publisher)
		self.mock_publisher.followers.add.assert_called_once_with(self.mock_user)

		self.mock_user_repo.save.assert_called_once_with(self.mock_user)
		self.mock_publisher_repo.save.assert_called_once_with(self.mock_publisher)


class UnFollowPublisherInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.UserRepository')
	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	def setUp(self, mock_user_repo, mock_publisher_repo):
		self.mock_user_repo = mock_user_repo
		self.mock_publisher_repo = mock_publisher_repo

		self.mock_user = mock.MagicMock(
			followers=mock.MagicMock(
				remove=mock.MagicMock()
			),
			already_following=mock.MagicMock(
				return_value=True
			)
		)

		self.mock_publisher = mock.MagicMock(
			id=123,
			followers=mock.MagicMock(
				remove=mock.MagicMock()
			)
		)

		self.mock_publisher_repo.get_one_by.return_value = self.mock_publisher

	def test_execute(self):
		interactor = UnFollowPublisherInteractor(
			user_repo=self.mock_user_repo,
			publisher_repo=self.mock_publisher_repo
		)
		interactor.execute(
			self.mock_user,
			self.mock_publisher.id
		)

		self.mock_user.already_following.assert_called_once_with(
			self.mock_publisher.id
		)

		self.mock_publisher_repo.get_one_by.assert_called_once_with(
			id=self.mock_publisher.id
		)

		self.mock_user.followers.remove.assert_called_once_with(self.mock_publisher)
		self.mock_publisher.followers.remove.assert_called_once_with(self.mock_user)

		self.mock_user_repo.save.assert_called_once_with(self.mock_user)
		self.mock_publisher_repo.save.assert_called_once_with(self.mock_publisher)


class UpdatePublisherProfileInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.ProductRepository')
	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	def setUp(self, mock_product_repo, mock_publisher_repo):
		self.mock_product_repo = mock_product_repo
		self.mock_publisher_repo = mock_publisher_repo

		self.mock_product = mock.MagicMock()
		self.mock_publisher = mock.MagicMock(
			bio='test',
			banner_text='',
			who_you_are='test',
			banner_product=self.mock_product
		)
		
		self.mock_product_repo.get_one_by.return_value = self.mock_product

	def test_execute(self):
		interactor = UpdatePublisherProfileInteractor(
			product_repo=self.mock_product_repo,
			publisher_repo=self.mock_publisher_repo
		)
		updated_publisher = interactor.execute(
			bio='test',
			who_you_are='test',
			banner_text='test',
			publisher=self.mock_publisher,
			banner_product=self.mock_product
		)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			id=self.mock_product
		)

		self.mock_publisher.bio='test'
		self.mock_publisher.banner_text='test'
		self.mock_publisher.who_you_are='test'
		self.mock_publisher.banner_product=self.mock_product

		self.mock_publisher_repo.save.assert_called_once_with(self.mock_publisher)

		self.assertEqual(updated_publisher, self.mock_publisher)


class UpdatePublisherProfileBannerImgInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	@mock.patch('elabodeal.api.repositories.FileRepository')
	def setUp(self, mock_publisher_repo, mock_file_repo):
		self.mock_publisher_repo = mock_publisher_repo
		self.mock_file_repo = mock_file_repo

		self.mock_file = mock.MagicMock()
		self.mock_publisher = mock.MagicMock(banner_img=None)

		self.mock_file_repo.add.return_value = self.mock_file

	def test_execute(self):
		interactor = UpdatePublisherProfileBannerImgInteractor(
			file_repo=self.mock_file_repo,
			publisher_repo=self.mock_publisher_repo
		)
		updated_publisher = interactor.execute(
			self.mock_publisher,
			self.mock_file
		)

		self.mock_file_repo.add.assert_called_once_with(
			self.mock_file,
			type='image'
		)

		self.mock_publisher.banner_img = self.mock_file

		self.mock_publisher_repo.save.assert_called_once_with(
			self.mock_publisher
		)

		self.assertEqual(updated_publisher, self.mock_publisher)


class UpdatePublisherProfileAvatarImgInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.PublisherRepository')
	@mock.patch('elabodeal.api.repositories.FileRepository')
	def setUp(self, mock_publisher_repo, mock_file_repo):
		self.mock_publisher_repo = mock_publisher_repo
		self.mock_file_repo = mock_file_repo

		self.mock_file = mock.MagicMock()
		self.mock_publisher = mock.MagicMock(avatar_img=None)

		self.mock_file_repo.add.return_value = self.mock_file

	def test_execute(self):
		interactor = UpdatePublisherProfileBannerImgInteractor(
			file_repo=self.mock_file_repo,
			publisher_repo=self.mock_publisher_repo
		)
		updated_publisher = interactor.execute(
			self.mock_publisher,
			self.mock_file
		)

		self.mock_file_repo.add.assert_called_once_with(
			self.mock_file,
			type='image'
		)

		self.mock_publisher.avatar_img = self.mock_file

		self.mock_publisher_repo.save.assert_called_once_with(
			self.mock_publisher
		)

		self.assertEqual(updated_publisher, self.mock_publisher)