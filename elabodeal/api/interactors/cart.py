from elabodeal.api.interactors import Interactor


class AddProductToCartInteractor(Interactor):
	def __init__(self, product_repo, cart_manager):
		self.product_repo = product_repo
		self.cart_manager = cart_manager

	def execute(self, product_id):
		product = self.product_repo.get_one_by(id=product_id)

		product_price = product.price

		self.cart_manager.add(product_id, product_price)
		self.cart_manager.commit()

		return product


class RemoveProductFromCartInteractor(Interactor):
	def __init__(self, cart_manager):
		self.cart_manager = cart_manager

	def execute(self, product_id):
		self.cart_manager.remove(product_id)
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








