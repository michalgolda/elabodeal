from elabodeal.api.interactors import Interactor


class AddProductToCartInteractor(Interactor):
	def __init__(self, product_repo, cart_manager):
		self.product_repo = product_repo
		self.cart_manager = cart_manager

	def execute(self, product_id):
		product = self.product_repo.get_one_by(id=product_id)

		product_id = str(product.id)
		product_title = product.title
		product_author = product.author
		product_price = float(product.price)
		product_cover_img_path = product.cover_img.path

		cart_manager_product = self.cart_manager.Product(
			id=product_id,
			price=product_price,
			title=product_title,
			author=product_author,
			cover_img_path=product_cover_img_path
		)

		self.cart_manager.add(cart_manager_product)
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
