from django.shortcuts import redirect
from django.contrib.postgres.search import SearchVector

from elabodeal.models import Product
from elabodeal.web.views import BaseView


class SearchResultsView(BaseView):
    def get(self, request):
        search_query = request.GET.get('search_query')
        
        if not search_query: return redirect('web:index')

        results = Product.objects \
                    .annotate(search=SearchVector('author', 'title')) \
                    .filter(search=search_query.lower()) \
                    .all()


        other_products = []

        if not results: other_products = Product.objects.all()[:4]

        context = {
            'results': results,
            'other_products': other_products
        }
        
        return self.respond('search-results.html', request, context)