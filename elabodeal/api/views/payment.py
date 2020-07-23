import stripe

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from elabodeal.api.serializers import NewPaymentIntentSerializer


class PaymentAPIView(APIView):
	def post(self, request):
		serializer = NewPaymentIntentSerializer(data=request.data)
		if not serializer.is_valid():
			errors = serializer.errors
			return Response(errors, 400)

		stripe.api_key = settings.STRIPE_API_KEY
		
		delivery = json.dumps(request.session['delivery'])
		products = json.dumps(request.session['cart']['products'])

		metadata={
			'delivery': delivery,
			'phone_number': serializer.data['phone_number'],
			'products': products
		}

		payment_intent = stripe.PaymentIntent.create(
			amount=int(float(request.session['cart']['total_price']) * 100),
			currency='PLN',
			metadata=metadata
		)

		return Response(payment_intent)