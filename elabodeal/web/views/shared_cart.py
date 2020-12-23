from django.shortcuts import redirect

from elabodeal.web.views import BaseView
from elabodeal.models import SharedCart


class SharedCartView(BaseView):
	def get(self, request, code):
		shared_cart = SharedCart.objects.filter(code=code).first()
		if not shared_cart:
			return redirect('web:index')

		shared_cart_items = shared_cart.cart.items.all()

		context = {
			'cart': shared_cart.cart,
			'cart_items': shared_cart_items,
			'shared_cart': shared_cart}

		return self.respond('shared_cart.html', request, context)