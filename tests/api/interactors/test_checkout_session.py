from unittest import mock
from tests import BaseTestCase

from django.core import mail
from django.test import override_settings

from elabodeal.api.interactors import (
    CreateCheckoutSessionInteractor,
	UpdateCheckoutSessionInteractor,
	RemoveCheckoutSessionInteractor,
	SucceedCheckoutSessionInteractor
)


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
	
	@mock.patch('elabodeal.utils.CartSessionManager')
	@mock.patch('elabodeal.api.repositories.ProductRepository')
	def setUp(self, mock_cart_manager, mock_product_repo):
		self.mock_product_repo = mock_product_repo
		self.mock_cart_manager = mock_cart_manager

		self.mock_user = mock.MagicMock(
			id=1,
			is_authenticated=True
		)
		self.mock_product = mock.MagicMock(
			id=1,
			title='test',
			author='test',
			price=20.00,
			cover_img=mock.MagicMock(
				path='test'
			)
		)

		self.mock_session = {
			'cart': {},
			'checkout_session': {
				'delivery': {
					'email': 'test@test.pl',
					'first_name': 'test'
				}
			}
		}

		type(self.mock_cart_manager).total_price_of_selected_products = mock.PropertyMock(
			return_value=2
		)
		type(self.mock_cart_manager).selected_products = mock.PropertyMock(
			return_value=[self.mock_product]
		)

		self.mock_product_repo.get_one_by.return_value = self.mock_product

		mail.outbox = []

	@override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
	def test_execute(self):
		interactor = SucceedCheckoutSessionInteractor(
			product_repo=self.mock_product_repo,
			cart_manager=self.mock_cart_manager
		)
		interactor.execute(
			user=self.mock_user,
			session=self.mock_session
		)

		self.mock_product_repo.get_one_by.assert_called_once_with(
			id=self.mock_product.id
		)

		self.assertEqual(len(mail.outbox), 1)