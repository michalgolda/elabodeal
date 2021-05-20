from django.shortcuts import redirect

from elabodeal.web.views import BaseView
from elabodeal.models import Category, Product


class IndexView(BaseView):
	def get(self, request):
		current_category = request.GET.get('c')

		categories = Category.objects.all()

		if current_category:
			category_exist = False
			for category in categories:
				if category.name.lower() == current_category.lower():
					category_exist = True
					break

			if not category_exist:
				return redirect('web:index')

			products = Product.objects \
				.filter(category__name=current_category) \
				.all()
		else:
			products = Product.objects.all()

		context = {
			'categories': categories,
			'products': products,
			'current_category': current_category
		}

		return self.respond('index.html', request, context)