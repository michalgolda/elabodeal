from elabodeal.api.interactors import Interactor


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


class ShareSavedCartInteractor(Interactor):
	def __init__(self, shared_cart_repo, cart_repo):
		self.cart_repo = cart_repo
		self.shared_cart_repo = shared_cart_repo

	def execute(self, cart_id):
		existing_cart = self.cart_repo.get_one_by(id=cart_id)

		shared_cart = self.shared_cart_repo.add(existing_cart)

		return shared_cart


class DeleteSavedCartInteractor(Interactor):
	def __init__(self, cart_repo):
		self.cart_repo = cart_repo

	def execute(self, user, cart_id):
		return self.cart_repo.delete_by(user=user, id=cart_id)
