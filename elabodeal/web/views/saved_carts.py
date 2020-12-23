from django.shortcuts import redirect

from elabodeal.web.views import BaseView, BaseAjaxView
from elabodeal.models import Cart, CartItem, Product, SharedCart


class SavedCartsView(BaseView):
	auth_required = True

	def get(self, request):
		user = request.user

		carts = Cart.objects.filter(user=user).all()

		context = {'carts': carts}

		return self.respond('saved_carts.html', request, context)


class SavedCartShareAjaxView(BaseAjaxView):
	auth_required = True

	def post(self, request):
		cart_id = request.POST.get('cart_id')

		saved_cart = Cart.objects.filter(id=cart_id).first()
		if not saved_cart or not cart_id:
			return self.respond(message='BadRequest',
								status=400)

		shared_cart = SharedCart.objects.create_share(cart=saved_cart)

		data = {'url': shared_cart.url}

		return self.respond(message='Success',
							data=data,
							status=201)


		