from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from elabodeal.models import Category, Product


class IndexView(View):
	def respond_index(self, request, context = None):
		return HttpResponse(render_to_string('index.html', context, request))

	def get(self, request):
		categories = Category.objects.all()
		products = Product.objects.all()

		for product in products:
			product.title = product.title[:30] + '...'

		context = {
			'categories': categories,
			'products': products
		}
		return self.respond_index(request, context)