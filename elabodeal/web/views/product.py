from elabodeal.web.views.base import BaseView
from elabodeal.models import Product


class ProductView(BaseView):
	def get_product_formats(self, product):
		product_files = product.files.all()

		product_formats = []
		for file in product_files:
			file_type = file.type
			file_extension = file.extension

			if file_type == 'ebook':
				product_formats.append(file_extension)

		return product_formats

	def get_context(self, product):
		return {
			'product': product,
			'product_formats': self.get_product_formats(product)
		}

	def get(self, request, id):
		product = Product.objects.filter(id=id).first()

		if not product:
			return self.respond('product_404.html', request)

		context = self.get_context(product)

		return self.respond('product.html', request, context)