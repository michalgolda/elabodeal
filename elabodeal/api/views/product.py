from rest_framework.views import APIView
from rest_framework.response import Response

from elabodeal.models import Product

from elabodeal.api.serializers import ProductUpdateSerializer


class ProductUpdateAPIView(APIView):
	def put(self, request, id):
		serializer = ProductUpdateSerializer(data=request.data)
		if not serializer.is_valid():
			errors = serializer.errors

			return Response(errors, status=400)

		product = Product.objects.filter(
			user__id=request.user.id, 
			id=id).first()

		if not product:
			return Response({
					'msg': 'Product does not exist.'
				}, status=400
			)

		for k, v in serializer.data.items():
			setattr(product, k, v)

		product.save()

		return Response(status=200)