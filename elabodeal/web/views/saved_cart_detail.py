from django.shortcuts import redirect

from elabodeal.web.views import BaseView, BaseAjaxView
from elabodeal.models import Cart, CartItem, Product


class SavedCartDetailView(BaseView):
	auth_required = True

	def get(self, request, id):
		cart = Cart.objects.filter(id=id).first()
		if not cart:
			return redirect('web:saved-carts')

		cart_items = cart.items.all()

		total_price = 0.00
		for item in cart_items:
			total_price += float(item.product.price)

		total_price = '{0:.2f}'.format(round(total_price, 2))

		context = {'items': cart_items,
				   'cart': cart,
				   'total_price': total_price}
		return self.respond('saved_cart_detail.html', request, context)