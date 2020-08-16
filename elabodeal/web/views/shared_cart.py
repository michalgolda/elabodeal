from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.models import SharedCart, SharedCartItem


class SharedCartView(BaseView):
	def get(self, request, code):
		shared_cart = SharedCart.objects.filter(code=code).first()
		if not shared_cart:
			return redirect('web:index')

		shared_cart_items = SharedCartItem.objects.filter(shared_cart__id=shared_cart.id).all()

		context = {
			'shared_cart': shared_cart,
			'shared_cart_items': shared_cart_items
		}
		return self.respond('shared_cart.html', request, context)