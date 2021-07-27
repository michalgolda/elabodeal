from django.shortcuts import redirect

from elabodeal.models import Cart, SharedCart
from elabodeal.web.views import BaseView


class SavedCartsView(BaseView):
	auth_required = True

	def get(self, request):
		user = request.user
		carts = Cart.objects.filter(user=user).all()

		context = { 'carts': carts }
		
		return self.respond('saved-carts.html', request, context)


class SavedCartDetailsView(BaseView):
	auth_required = True

	def get(self, request, id):
		user = request.user
		existing_cart = Cart.objects.filter(user=user, id=id).first()

		if not existing_cart: return redirect('web:index')

		existing_cart_products = existing_cart.products.all()
		exisitng_shared_cart = SharedCart.objects.filter(cart=existing_cart).first()

		serialized_existing_shared_cart = {
			'code': exisitng_shared_cart.code
		} if exisitng_shared_cart else None

		context = {
			'cart': existing_cart,
			'products': existing_cart_products,
			'application_data': {
				'sc': serialized_existing_shared_cart
			}
		}

		return self.respond('saved-cart-details.html', request, context)