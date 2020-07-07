from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from elabodeal.models import Product


class CartView(View):
	def respond_cart(self, request, context = None):
		return HttpResponse(render_to_string('cart.html', context, request))

	def get(self, request):
		products = Product.objects.all()

		context = {
			'products': [products[0]]
		}
		return self.respond_cart(request, context)