from elabodeal.web.views.base import BaseView
from elabodeal.models import PurchasedProduct

class MyBooksView(BaseView):
	auth_required = True

	def get(self, request):
		purchased_products = PurchasedProduct.objects.filter(user__id=request.user.id).all()

		context = {
			'products': purchased_products
		}
		return self.respond('my_books.html', request, context)