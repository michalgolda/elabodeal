from elabodeal.web.views.base import BaseView

from elabodeal.models import Product


class SalesManagerView(BaseView):
	auth_required = True
	seller_required = True

	def get(self, request):
		products = Product.objects.filter(author__username=request.user.username).all()

		context = {
			'products': products if len(products) > 0 else False
		}
		return self.respond('salesmanager/index.html', request, context)