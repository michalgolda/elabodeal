from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from elabodeal.models import Product


class ProductDetailView(View):
	def respond_index(self, request, context = None):
		return HttpResponse(render_to_string('product_detail.html', context, request))

	def respond_404(self, request, context = None):
		return HttpResponse(render_to_string('product_404.html', context, request))
	
	def get(self, request, id):
		product = Product.objects.filter(id=id).first()
		if not product:
			return self.respond_404(request)

		products = Product.objects.all()
		for p in products:
			p.title = p.title[:30] + '...'

		context = {
			'product': product,
			'related_products': products
		}
		return self.respond_index(request, context)