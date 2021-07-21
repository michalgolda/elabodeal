from unittest import mock
from tests import BaseTestCase

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
	pass