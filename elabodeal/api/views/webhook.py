import json
import stripe

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response


class WebHookAPIView(APIView):
	def post(self, request):
		sig_header = request.META['HTTP_STRIPE_SIGNATURE']
		secret = settings.STRIPE_WEBHOOK_SECRET

		try:
			event = stripe.Event.construct_from(
				request.data, sig_header, secret
			)
		except ValueError:
			return Response(status=400)
		except stripe.error.SignatureVerificationError:
			return Response(status=400)

		return Response(status=400)