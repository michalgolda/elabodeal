from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.models import Cart, CartItem, Product


class SavedCartDetailView(BaseView):
	auth_required = True

	def get(self, request, id):
		# cart = Cart.objects.filter(id=id).first()
		# if not cart:
		# 	return redirect('web:saved-carts')

		# cart_items = CartItem.objects.filter(cart__id=id).all()
		# total_price = 0.00
		# for item in cart_items:
		# 	total_price += float(item.product.price)

		# total_price = '{0:.2f}'.format(round(total_price, 2))

		# context = {
		# 	'cart': cart,
		# 	'cart_items': cart_items,
		# 	'total_price': total_price
		# }
		context = {}
		return self.respond('saved_cart_detail.html', request, context)


	def post(self, request, id):
		cart = Cart.objects.filter(id=id).first()
		if not cart:
			return redirect('web:saved-carts')

		cart.delete()

		return redirect('web:saved-carts')
