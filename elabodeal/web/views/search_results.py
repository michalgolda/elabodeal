from django.shortcuts import redirect
from django.contrib.postgres.search import SearchVector

from elabodeal.models import Product
from elabodeal.web.views import BaseView


class SearchResultsView(BaseView):
    def get(self, request):
        search_query = request.GET.get('query')
        if not search_query:
            return redirect('web:index')

        results = Product.objects.annotate(
            search=SearchVector('author', 'title')
            ).filter(search=search_query.lower()).all()

        context = {'results': results}
        
        return self.respond('search_results.html', request, context)