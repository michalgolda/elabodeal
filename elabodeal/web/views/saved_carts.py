from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.models import Cart, CartItem, Product


class SavedCartsView(BaseView):
	auth_required = True

	def get(self, request):
		carts = Cart.objects.filter(user__id=request.user.id).all()

		context = {
			'carts': carts if len(carts) > 0 else False
		}
		return self.respond('saved_carts.html', request, context)

	def post(self, request):
		action_type = request.POST.get('action_type')

		if action_type == 'delete-cart':
			cart_id = request.POST.get('cart_id')

			cart = Cart.objects.filter(id=cart_id).first()
			cart.delete()

			return redirect('web:saved-carts')