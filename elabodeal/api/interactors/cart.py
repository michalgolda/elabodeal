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




