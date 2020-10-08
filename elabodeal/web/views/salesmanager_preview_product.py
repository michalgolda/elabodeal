import json
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from elabodeal.web.views.base import BaseView
from elabodeal.models import Product

from elabodeal.api.serializers import ProductUpdateSerializer


class SalesManagerPreviewProductView(BaseView):
	auth_required = True
	seller_required = True

	def get(self, request, id):
		product = Product.objects.filter(
			user__id=request.user.id, 
			id=id).first()

		if not product:
			return redirect('web:salesmanager')

		product_update_serializer = ProductUpdateSerializer(product)

		context = {
			'product': product,
			'fields_for_update': mark_safe(
				json.dumps(product_update_serializer.data)
			)
		}
		return self.respond(
			'salesmanager/preview_product.html', 
			request, 
			context
		)