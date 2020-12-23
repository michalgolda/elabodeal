from elabodeal.web.views.base import BaseView
from elabodeal.models import PurchasedProduct

class PurchasedProductsView(BaseView):
	auth_required = True

	def get(self, request):
		user = request.user

		purchased_products = PurchasedProduct.objects.filter(user=user).all()

		context = {'purchased_products': purchased_products}

		return self.respond('purchased_products.html', request, context)