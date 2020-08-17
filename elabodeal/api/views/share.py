from rest_framework.views import APIView
from rest_framework.response import Response

from elabodeal.api.serializers import ShareCartSerializer

from elabodeal.models import SharedCart, SharedCartItem, Product


class ShareCartAPIView(APIView):
	def post(self, request):
		serializer = ShareCartSerializer(data=request.data)
		if not serializer.is_valid():
			errors = serializer.errors
			return Response(errors, status=400)

		cart = request.session['cart']

		shared_cart_code = SharedCart.generate_code()
		shared_cart = SharedCart(
			code=shared_cart_code,
			title=serializer.data['title'],
			description=serializer.data['description']
		)
		shared_cart.save()
		
		for cart_item in cart['products']:
			product = Product.objects.filter(id=cart_item['id']).first()
			shared_cart_item = SharedCartItem(shared_cart=shared_cart, product=product)
			shared_cart_item.save()

		return Response({'shared_cart_code': shared_cart_code}, status=201)