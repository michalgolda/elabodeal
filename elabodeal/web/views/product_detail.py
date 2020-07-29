from elabodeal.web.views.base import BaseView
from elabodeal.models import Product


class ProductDetailView(BaseView):
	def get(self, request, url_name: str):
		product = Product.objects.filter(url_name=url_name).first()
		if not product:
			return self.respond('product_404.html', request)

		products = Product.objects.all()
		for p in products:
			if len(p.title) >= 30:
				p.title = p.title[:30] + '...'

		if not 'counted_view' in request.session:
			product.count_views += 1
			product.save()
			request.session['counted_view'] = True

		context = {
			'product': product,
			'related_products': products[:4]
		}
		return self.respond('product_detail.html', request, context)