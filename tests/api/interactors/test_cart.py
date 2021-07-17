from unittest import mock
from tests import BaseTestCase

from elabodeal.api.interactors import (
	SaveCartInteractor,
	AddProductToCartInteractor,
	RemoveProductFromCartInteractor,
	CreateCheckoutSessionInteractor,
	UpdateCheckoutSessionInteractor,
	RemoveCheckoutSessionInteractor,
	SucceedCheckoutSessionInteractor,
	SelectOrDeselectCartProductInteractor,
)


class AddProductToCartInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.utils.CartSessionManager')
	@mock.patch('elabodeal.api.repositories.ProductRepository')
	def setUp(self, mock_cart_manager, mock_product_repo):
		self.mock_cart_manager = mock_cart_manager
		self.mock_product_repo = mock_product_repo

	def test_execute(self):
		mock_product = mock.MagicMock(id='1', price=1)

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

		self.mock_cart_manager.remove.assert_called_once_with('1')
		self.mock_cart_manager.commit.assert_called()


class SaveCartInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.api.repositories.CartRepository')
	@mock.patch('elabodeal.utils.session.CartSessionManager')
	@mock.patch('elabodeal.api.repositories.ProductRepository')
	def setUp(self, mock_cart_repo, mock_cart_manager, mock_product_repo):
		self.mock_cart_repo = mock_cart_repo
		self.mock_cart_manager = mock_cart_manager
		self.mock_product_repo = mock_product_repo

	def test_execute(self):
		mock_user = mock.MagicMock()

		mock_cart = mock.MagicMock()
		mock_cart.products.add = mock.MagicMock()

		self.mock_cart_repo.add.return_value = mock_cart

		mock_cart_session_product = self.mock_cart_manager.Product(1, 1)

		self.mock_cart_manager.products = [mock_cart_session_product]

		mock_product = mock.MagicMock()

		self.mock_product_repo.get_one_by.return_value = mock_product

		interactor = SaveCartInteractor(
			cart_repo=self.mock_cart_repo,
			product_repo=self.mock_product_repo,
			cart_manager=self.mock_cart_manager
		)

		interactor.execute(
			user=mock_user,
			title='test',
			description='test'
		)

		self.mock_cart_repo.add.assert_called_once_with(
			user=mock_user,
			title='test',
			description='test'
		)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			id=mock_cart_session_product.id
		)

		mock_cart.products.add.assert_called_once_with(mock_product)

		self.mock_cart_repo.save.assert_called_once_with(mock_cart)


class SelectOrDeselectCartProductInteractorTest(BaseTestCase):

	@mock.patch('elabodeal.utils.session.CartSessionManager')
	def setUp(self, mock_cart_manager):
		self.mock_cart_manager = mock_cart_manager

	def test_execute(self):
		self.mock_cart_manager.product_is_selected.return_value = True

		interactor = SelectOrDeselectCartProductInteractor(
			cart_manager=self.mock_cart_manager
		)
		interactor.execute(1)

		self.mock_cart_manager.deselect.assert_called_once_with('1')

		self.mock_cart_manager.product_is_selected.return_value = False

		interactor.execute(1)

		self.mock_cart_manager.product_is_selected.assert_called_with('1')
		self.mock_cart_manager.select.assert_called_once_with('1')

		self.mock_cart_manager.commit.assert_called()


class CreateCheckoutSessionInteractorTest(BaseTestCase):
	
	@mock.patch('elabodeal.utils.session.CartSessionManager')
	@mock.patch('elabodeal.api.services.StripePaymentService')
	def setUp(self, mock_cart_manager, mock_payment_service):
		self.mock_cart_manager = mock_cart_manager
		self.mock_payment_service = mock_payment_service

	def test_execute(self):
		session = {}

		mock_payment_intent = dict(
			id='123',
			client_secret='123'
		)

		self.mock_payment_service.create_payment_intent.return_value = mock_payment_intent
		self.mock_cart_manager.total_price_of_selected_products.return_value = '2.00'

		interactor = CreateCheckoutSessionInteractor(
			cart_manager=self.mock_cart_manager,
			payment_service=self.mock_payment_service
		)
		checkout_session = interactor.execute(session)

		self.mock_cart_manager.total_price_of_selected_products.assert_called
		self.mock_payment_service.create_payment_intent.assert_called_once_with(
			amount=100,
			currency='pln'
		)

		self.assertIn('id', checkout_session)
		self.assertIn('cid', checkout_session)
		self.assertEqual(checkout_session.get('step'), 'deliver')
		self.assertEqual(checkout_session.get('pi'), '123')
		self.assertEqual(checkout_session.get('cs'), '123')


class UpdateCheckoutSessionInteractorTest(BaseTestCase):
	def test_execute(self):
		session = dict(
			checkout_session=dict(
				step='deliver'
			)
		)

		delivery = dict(
			first_name='test',
			last_name='test',
			email='test'
		)

		interactor = UpdateCheckoutSessionInteractor()
		checkout_session = interactor.execute(
			session=session,
			first_name=delivery.get('first_name'),
			last_name=delivery.get('last_name'),
			email=delivery.get('email')
		)

		self.assertEqual(checkout_session.get('step'), 'payment')
		self.assertEqual(checkout_session.get('delivery'), delivery)


class RemoveCheckoutSessionInteractorTest(BaseTestCase):
	
	@mock.patch('elabodeal.api.services.StripePaymentService')
	def setUp(self, mock_payment_service):
		self.mock_payment_service = mock_payment_service

	def test_execute(self):
		session = dict(
			checkout_session=dict(
				pi='123'
			)
		)

		interactor = RemoveCheckoutSessionInteractor(
			payment_service=self.mock_payment_service
		)
		interactor.execute(session)

		self.mock_payment_service.cancel_payment_intent.assert_called_once_with(
			'123'
		)

		self.assertEqual(session, {})


class SucceedCheckoutSessionInteractorTest(BaseTestCase):
	pass