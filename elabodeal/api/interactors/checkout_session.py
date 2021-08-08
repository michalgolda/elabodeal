import uuid

from elabodeal.celery.tasks import send_email
from elabodeal.api.interactors import Interactor
from elabodeal.emails import PurchaseConfirmationEmailDTO


class CreateCheckoutSessionInteractor(Interactor):
	def __init__(self, cart_manager, payment_service):
		self.cart_manager = cart_manager
		self.payment_service = payment_service

	def execute(self, session):
		payment_intent = self.payment_service.create_payment_intent(
			amount=int(float(self.cart_manager.total_price_of_selected_products) * 100),
			currency='pln'
		)
		payment_intent_id = payment_intent['id']
		payment_intent_client_secret = payment_intent['client_secret']

		checkout_session = {
			'id': str(uuid.uuid4()),
			'cid': self.cart_manager.id,
			'step': 'deliver',
			'pi': payment_intent_id,
			'cs': payment_intent_client_secret
		}

		session['checkout_session'] = checkout_session

		return checkout_session


class UpdateCheckoutSessionInteractor(Interactor):
	def execute(self, session, first_name, last_name, email):
		checkout_session = session['checkout_session']

		checkout_session['step'] = 'payment'

		checkout_session['delivery'] = dict(
			first_name=first_name,
			last_name=last_name,
			email=email
		)

		session['checkout_session'] = checkout_session

		return checkout_session


class RemoveCheckoutSessionInteractor(Interactor):
	def __init__(self, payment_service):
		self.payment_service = payment_service

	def execute(self, session):
		checkout_session = session['checkout_session']
		payment_intent_id = checkout_session['pi']

		self.payment_service.cancel_payment_intent(payment_intent_id)

		del session['checkout_session']


class SucceedCheckoutSessionInteractor(Interactor):
	def __init__(self, cart_manager, product_repo, purchased_product_repo):
		self.product_repo = product_repo
		self.cart_manager = cart_manager
		self.purchased_product_repo = purchased_product_repo

	def execute(self, user, session):
		checkout_session = session['checkout_session']
		checkout_session_delivery = checkout_session['delivery']

		buyer_email = checkout_session_delivery['email']
		buyer_first_name = checkout_session_delivery['first_name']
		total_price = self.cart_manager.total_price_of_selected_products

		purchased_products = []
		cart_products = self.cart_manager.selected_products

		for cart_product in cart_products:
			cart_product_id = cart_product.id

			product = self.product_repo.get_one_by(id=cart_product_id)

			if user.is_authenticated:
				self.purchased_product_repo.add(user=user, product=product)

			purchased_products.append({
				'title': product.title,
				'price': float(product.price),
				'author': product.author,
				'cover_img_path': product.cover_img.path
			})

		email_template_context = {
			'total_price': total_price,
			'buyer_first_name': buyer_first_name,
			'purchased_products': purchased_products,
			'userIsAuthenticated': user.is_authenticated
		}

		email_dto = PurchaseConfirmationEmailDTO(
			to=buyer_email,
			context=email_template_context
		)

		serialized_email_dto = email_dto.asdict()

		send_email.delay(serialized_email_dto)

		del session['cart']
		del session['checkout_session']