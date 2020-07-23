import json
import stripe

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.response import Response

from elabodeal.models import User, PurchasedProduct, Product


class WebHookAPIView(APIView):
	def post(self, request):
		try:
			sig_header = request.META['HTTP_STRIPE_SIGNATURE']
		except KeyError:
			return Response(status=403)

		secret = settings.STRIPE_WEBHOOK_SECRET

		try:
			event = stripe.Event.construct_from(
				request.data, sig_header, secret
			)
		except ValueError:
			return Response(status=403)
		except stripe.error.SignatureVerificationError:
			return Response(status=403)

		if event.type == 'payment_intent.succeeded':
			metadata = event.data.object.metadata;

			delivery = json.loads(metadata['delivery'])
			products = json.loads(metadata['products'])

			user = User.objects.filter(email=delivery['email']).first()
			if user:
				for p in products:
					product = Product.objects.filter(id=p['id']).first()
					has_purchased_product = PurchasedProduct.objects.filter(product__id=p['id']).first()
					if not has_purchased_product:
						purchased_product = PurchasedProduct(
							user=user,
							product=product
						)
						purchased_product.save()

			if delivery['gift']:
				send_mail(
					subject='Elabodeal - Prezent',
					message=f'Dostałeś prezent',
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=[delivery['gift_email']],
					html_message=render_to_string('emails/gift.html', {'email': delivery['gift_email']})
				)				

			send_mail(
				subject='Elabodeal - Nowa transakcja',
				message=f'Dziękujemy za zakupy',
				from_email=settings.EMAIL_HOST_USER,
				recipient_list=[delivery['email']],
				html_message=render_to_string('emails/new_transaction.html')
			)

		return Response(status=200)