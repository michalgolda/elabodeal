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

		# Count view increment
		if not 'viewed_products' in request.session:
			request.session['viewed_products'] = []
			
		viewed_products = request.session['viewed_products']
		if not product.id in viewed_products:
			viewed_products.append(product.id)
			request.session['viewed_products'] = viewed_products

			product.count_views += 1
			product.save()

		related_products = products[:4]
		for p in related_products:
			p.empty_stars = range(5 - int(p.rating))
			p.rating = range(int(p.rating))


		show_add_product_info = request.session['show_add_product_info']
		request.session['show_add_product_info'] = False

		context = {
			'product': product,
			'related_products': related_products,
			'show_add_product_info': show_add_product_info
		}
		return self.respond('product_detail.html', request, context)