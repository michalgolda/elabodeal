import stripe

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from elabodeal.api.serializers import NewPaymentIntentSerailizer


class PaymentAPIView(APIView):
	def post(self, request):
		serializer = NewPaymentIntentSerailizer(data=request.data)
		if not serializer.is_valid():
			errors = serializer.errors
			return Response(errors, 400)

		stripe.api_key = settings.STRIPE_API_KEY
		
		payment_intent = stripe.PaymentIntent.create(
			amount=int(float(request.session['cart']['total_price']) * 100),
			currency='PLN',
			metadata={
				'first_name': serializer.data['first_name'],
				'last_name': serializer.data['last_name'],
				'email': serializer.data['email'],
				'phone_number': serializer.data['phone_number'],
			}
		)

		return Response(payment_intent)