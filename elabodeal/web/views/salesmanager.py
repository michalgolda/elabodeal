from elabodeal.web.views.base import BaseView

from elabodeal.models import Product


class SalesManagerView(BaseView):
	auth_required = True
	seller_required = True

	def get(self, request):
		products = Product.objects.filter(author__username=request.user.username).all()

		for p in products:
			if len(p.title) > 117:
				p.title = p.title[:114] + '...'

		context = {
			'products': products if len(products) > 0 else False
		}
		return self.respond('salesmanager/index.html', request, context)