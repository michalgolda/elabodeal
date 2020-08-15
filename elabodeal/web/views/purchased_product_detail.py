from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.models import PurchasedProduct


class PurchasedProductDetailView(BaseView):
	auth_required = True

	def get(self, request, id):
		purchased_product = PurchasedProduct.objects.filter(product__id=id, user__id=request.user.id).first()
		if not purchased_product:
			return redirect('web:my-books')

		context = {
			'product': purchased_product.product,
			'purchased_product': purchased_product
		}
		return self.respond('purchased_product_detail.html', request, context)


	def post(self, request, id):
		purchased_product = PurchasedProduct.objects.filter(product__id=id, user__id=request.user.id).first()
		if not purchased_product:
			return redirect('web:my-books')

		rating_for_set = int(request.POST.get('rating'))

		if purchased_product.review:
			rating = (purchased_product.product.rating - purchased_product.set_rating) + rating_for_set
			purchased_product.product.rating = round(rating, 2)
			purchased_product.product.save()
			purchased_product.set_rating = rating_for_set
			purchased_product.save()

			return redirect('web:purchased-product-detail', id=id)

		purchased_product.product.reviews += 1
		rating = (purchased_product.product.rating + rating_for_set) / purchased_product.product.reviews
		purchased_product.product.rating = round(rating, 2)
		purchased_product.product.save()
		purchased_product.review = True
		purchased_product.set_rating = rating_for_set
		purchased_product.save()

		return redirect('web:purchased-product-detail', id=id)
			
