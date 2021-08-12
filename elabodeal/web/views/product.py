from elabodeal.web.views.base import BaseView
from elabodeal.models import (
	Product,
	PurchasedProduct
)


class ProductView(BaseView):
	def get(self, request, id):
		product = Product.objects.filter(id=id).first()

		if not product:
			return self.respond('product_404.html', request)

		product_files = product.files.all()

		product_formats = []
		for file in product_files:
			file_type = file.type
			file_extension = file.extension

			if file_type == 'ebook':
				product_formats.append(file_extension)

		user = request.user
		user_has_product = False

		if user.is_authenticated:
			user_has_product = PurchasedProduct.objects.filter(product=product).exists()		

		context = {
			'product': product,
			'product_formats': product_formats,
			'user_has_product': user_has_product
		}

		return self.respond('product.html', request, context)