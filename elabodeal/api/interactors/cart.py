import uuid
from elabodeal.api.interactors import Interactor


class AddProductToCartInteractor(Interactor):
	def __init__(self, product_repo, cart_manager):
		self.product_repo = product_repo
		self.cart_manager = cart_manager

	def execute(self, product_id):
		product = self.product_repo.get_one_by(id=product_id)

		product_price = product.price

		self.cart_manager.add(str(product_id), float(product_price))
		self.cart_manager.commit()

		return product


class RemoveProductFromCartInteractor(Interactor):
	def __init__(self, cart_manager):
		self.cart_manager = cart_manager

	def execute(self, product_id):
		self.cart_manager.remove(str(product_id))
		self.cart_manager.commit()


class SaveCartInteractor(Interactor):
	def __init__(self, cart_repo, product_repo, cart_manager):
		self.cart_repo = cart_repo
		self.product_repo = product_repo
		self.cart_manager = cart_manager

	def execute(self, user, title, description):
		cart = self.cart_repo.add(
			user=user,
			title=title,
			description=description
		)

		cart_session_products = self.cart_manager.products

		for cart_session_product in cart_session_products:
			product = self.product_repo.get_one_by(id=cart_session_product.id)

			cart.products.add(product)

		self.cart_repo.save(cart)


class SelectOrDeselectCartProductInteractor(Interactor):
	def __init__(self, cart_manager):
		self.cart_manager = cart_manager

	def execute(self, product_id):
		product_is_selected = self.cart_manager.product_is_selected(str(product_id))

		if product_is_selected: self.cart_manager.deselect(str(product_id))
		else: self.cart_manager.select(str(product_id))
		
		self.cart_manager.commit()

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
	def execute(self, session):
		del session['cart']
		del session['checkout_session']
