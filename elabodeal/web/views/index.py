from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from elabodeal.models import Category, Product


class IndexView(View):
	def respond_index(self, request, context = None):
		return HttpResponse(render_to_string('index.html', context, request))

	def get(self, request):
		categories = Category.objects.all()

		category_param = request.GET.get('category')
		if not category_param:
			products = Product.objects.all()

		# Check if category does exisit in db
		category = Category.objects.filter(name=category_param).first()
		if not category:
			products = Product.objects.all()
		else:
			products = Product.objects.filter(category__name=category_param).all()

		for product in products:
			product.title = product.title[:30] + '...'

		context = {
			'categories': categories,
			'products': products
		}
		return self.respond_index(request, context)