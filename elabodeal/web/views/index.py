from django.contrib.postgres.search import SearchVector

from elabodeal.web.views.base import BaseView
from elabodeal.models import Category, Product


class IndexView(BaseView):
	def get(self, request):
		categories = Category.objects.all()

		category_param = request.GET.get('category')
		search_query = request.GET.get('q')

		use_search = False

		if category_param:
			products = Product.objects.filter(category__name=category_param).all()
		elif search_query:
			products = Product.objects.annotate(
				search=SearchVector('author__first_name', 'author__last_name', 'title')
			).filter(search=search_query.lower()).all()

			use_search = True
		else:
			products = Product.objects.all()

		for p in products:
			p.title = p.title[:30] + '...'

		for p in products:
			p.empty_stars = range(5 - int(p.rating))
			p.rating = range(int(p.rating))

		context = {
			'categories': categories,
			'products': products if len(products) > 0 else False,
			'use_search': use_search,
			'search_query': search_query if search_query else "",
			'category_param': category_param,
		}

		return self.respond('index.html', request, context)