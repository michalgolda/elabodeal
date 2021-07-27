from django.shortcuts import redirect

from elabodeal.web.views import BaseView
from elabodeal.models import SharedCart


class SharedCartView(BaseView):
	def get(self, request, code):
		existing_shared_cart = SharedCart.objects.filter(code=code).first()
		
		if not existing_shared_cart: return redirect('web:index')

		existing_cart = existing_shared_cart.cart
		existing_cart_products = existing_cart.products.all()

		context = {
			'cart': existing_cart,
			'products': existing_cart_products,
			'shared_cart': existing_shared_cart
		}

		return self.respond('shared-cart.html', request, context)