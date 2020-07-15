from elabodeal.web.views.base import BaseView
from elabodeal.models import Product


class ProductDetailView(BaseView):
	def get(self, request, id):
		product = Product.objects.filter(id=id).first()
		if not product:
			return self.respond('product_404.html', request)

		products = Product.objects.all()
		for p in products:
			p.title = p.title[:30] + '...'

		context = {
			'product': product,
			'related_products': products[:4]
		}
		return self.respond('product_detail.html', request, context)