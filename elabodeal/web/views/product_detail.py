from elabodeal.web.views.base import BaseView
from elabodeal.models import Product


class ProductDetailView(BaseView):
	def get(self, request, url_name: str):
		product = Product.objects.filter(url_name=url_name).first()
		if not product:
			return self.respond('product_404.html', request)

		session = request.session

		viewed_products = session.get('viewed_products')
		if not viewed_products:
			viewed_products = []
			
		if not product.id in viewed_products:
			viewed_products.append(product.id)
			session['viewed_products'] = viewed_products

			product.views += 1
			product.save()

		related_products = Product.objects.all()
		related_products = related_products[:4]

		cart_update_popup = session.get('cart_update_popup')
		if cart_update_popup:
			session['cart_update_popup'] = False

		request.session = session

		context = {
			'product': product,
			'related_products': related_products,
			'cart_update_popup': cart_update_popup
		}
		return self.respond('product_detail.html', request, context)