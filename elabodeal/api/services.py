import stripe
from django.conf import settings
from abc import ABC, abstractmethod


class PaymentService(ABC):

	@abstractmethod
	def create_payment_intent(self, amount, currency):
		raise NotImplementedError


class StripePaymentService(PaymentService):
	
	def __init__(self):
		self.client = stripe
		self.client.api_key = settings.STRIPE_SECRET_KEY

	def create_payment_intent(self, amount, currency):
		return self.client.PaymentIntent.create(
			amount=amount,
			currency=currency,
			payment_method_types=['card']
		)

	def cancel_payment_intent(self, payment_intent_id):
		return self.client.PaymentIntent.cancel(payment_intent_id)