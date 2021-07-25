from elabodeal.api.interactors import Interactor


class AddProductToCartInteractor(Interactor):
	def __init__(self, product_repo, cart_manager):
		self.product_repo = product_repo
		self.cart_manager = cart_manager

	def execute(self, product_id, clear):
		product = self.product_repo.get_one_by(id=product_id)

		product_price = product.price

		if clear: self.cart_manager.clear()

		self.cart_manager.add(str(product_id), float(product_price))
		self.cart_manager.commit()

		return product


class RemoveProductFromCartInteractor(Interactor):
	def __init__(self, cart_manager):
		self.cart_manager = cart_manager

	def execute(self, product_id):
		self.cart_manager.remove(str(product_id))
		self.cart_manager.commit()


class SelectOrDeselectCartProductInteractor(Interactor):
	def __init__(self, cart_manager):
		self.cart_manager = cart_manager

	def execute(self, product_id):
		product_is_selected = self.cart_manager.product_is_selected(str(product_id))

		if product_is_selected: self.cart_manager.deselect(str(product_id))
		else: self.cart_manager.select(str(product_id))
		
		self.cart_manager.commit()
