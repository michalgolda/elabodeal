from elabodeal.models import Product
from elabodeal.web.views import BaseView


class SalesManagerIndexView(BaseView):
	auth_required = True
	publisher_required = True

	def get(self, request):
		user = request.user
		publisher = user.publisher

		products = Product.objects.filter(publisher=publisher).all()

		context = {'products': products}

		return self.respond('salesmanager/index.html', request, context)