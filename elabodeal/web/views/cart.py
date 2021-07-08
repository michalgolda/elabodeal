import stripe
import json

from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.template.loader import render_to_string

from elabodeal.web.views import BaseView, BaseAjaxView
from elabodeal.web.forms import DeliveryForm
from elabodeal.models import Product, Cart, PurchasedProduct, User
# from elabodeal.utils import SessionCartManager


class CartView(BaseView):
	def get(self, request):
		cart = SessionCartManager(request)
		
		products = []
		for item in cart.items:
			product = Product.objects.filter(id=item.id).first()

			products.append(product)

		context = {'products': products}

		return self.respond('cart.html', request, context)


class CartCheckoutDeliveryView(BaseView):
	def get_form(self, request = None):
		return DeliveryForm(request.POST if request else request)

	def get(self, request):
		session = request.session

		cart = session.get('cart')
		if not cart or not cart['item_count'] > 0:
			return redirect('web:cart')

		context = {'form': self.get_form()}

		return self.respond('cart-checkout-delivery.html', request, context)

	def post(self, request):
		session = request.session

		form = self.get_form(request)

		if form.is_valid():
			cart = session['cart']

			products = cart['items']
			total_price = cart['total_price']
			delivery = form.cleaned_data

			session['checkout-payment']	= True
			session['checkout-data'] = {'delivery': delivery,
										'products': products, 
										'total_price': total_price}

			request.session = session

			return redirect('web:cart-checkout-payment')

		context = {'form': form}

		return self.respond('cart-checkout-delivery.html', request, context)


class CartCheckoutPaymentView(BaseView):
	def get(self, request):
		session = request.session

		checkout_payment = session.get('checkout-payment')
		if not checkout_payment:
			return redirect('web:cart-checkout-delivery')

		return self.respond('cart-checkout-payment.html', request)


class CartCheckoutPaymentAjaxView(BaseAjaxView):	
	def post(self, request):
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone_number = request.POST.get('phone_number')

		if (not email or not first_name
			or not last_name or not phone_number):
			return self.respond(message='BadRequest',
								status=400)

		stripe.api_key = settings.STRIPE_API_KEY

		session = request.session

		checkout_data = session['checkout-data']
		
		metadata_delivery = json.dumps(checkout_data['delivery'])
		metadata_products = json.dumps(checkout_data['products'])
		metadata_payer = json.dumps({'email': email,
									 'first_name': first_name,
									 'last_name': last_name,
									 'phone_number': phone_number})

		metadata = {'delivery': metadata_delivery,
					'products': metadata_products,
					'payer': metadata_payer}

		total_price = checkout_data['total_price']

		amount = int(float(total_price) * 100)

		payment_intent = stripe.PaymentIntent.create(amount=amount,
													 currency='PLN',
													 metadata=metadata)

		return self.respond(message="Success",
							data=payment_intent,
							status=201)

@method_decorator(csrf_exempt, name='dispatch')
class CartCheckoutPaymentSuccessView(BaseView):
	def get(self, request):
		session = request.session

		checkout_data = session.get('checkout-data')
		if not checkout_data:
			return redirect('web:index')

		delivery = checkout_data['delivery']
		delivery_email = delivery['email']

		context = {'delivery_email': delivery_email}

		del session['checkout-data']
		del session['cart']

		return self.respond('cart-checkout-payment-success.html', request, context)

	def post(self, request):
		try:
			sig_header = request.META['HTTP_STRIPE_SIGNATURE']
		except KeyError as e:
			return Response(status=403)

		secret = settings.STRIPE_WEBHOOK_SECRET
		payload = request.body

		try:
			event = stripe.Event.construct_from(json.loads(payload), 
												sig_header, secret)
		except ValueError as e:
			return HttpResponse(status=400)
		except stripe.error.SignatureVerificationError as e:
			return HttpResponse(status=400)

		if event.type == 'payment_intent.succeeded':
			event_metadata = event.data.object.metadata

			delivery = json.loads(event_metadata['delivery'])
			products = json.loads(event_metadata['products'])
			payer = json.loads(event_metadata['payer']) 

			delivery_email = delivery['email']

			user = User.objects.filter(email=delivery_email).first()

			product_objects = []
			for p in products:
				product_id = p['id']

				product_object = Product.objects.filter(id=product_id).first()
				product_objects.append(product_object)

				if user:
					has_purchased_product = PurchasedProduct.objects.filter(product=product_object, user=user).first()
					if not has_purchased_product:
						purchased_product = PurchasedProduct(user=user, product=product_object)
						purchased_product.save()

			# TODO: Dodanie taska celery wysyłającego maila
			amount = event.data.object.amount
			total_price = '{0:.2f}'.format(round(amount / 100, 2))

			context_of_email = {'products': product_objects,
								'total_price': total_price,
								'payment_method': 'Karta płatnicza'}

			send_mail(subject='Elabodeal - Potwierdzenie zakupu ebooka',
					  message='Dziękujemy za zakupy',
					  from_email=settings.EMAIL_HOST_USER,
					  recipient_list=[delivery_email],
					  html_message=render_to_string('emails/payment_success.html', context_of_email))

		return HttpResponse(status=200)


# class CartAddItemAction(BaseView):
# 	def post(self, request):
# 		product_id = request.POST.get('product_id')
		
# 		product = Product.objects.filter(id=int(product_id)).first()
# 		if not product:
# 			return redirect('web:index')

# 		cart = SessionCartManager(request)

# 		for item in cart.items:
# 			if item.id == product.id:
# 				return redirect('web:product-detail', 
# 								url_name=product.url_name)

# 		cart_item = cart.Item(id=product.id, 
# 							  price=float(product.price))
# 		cart.add_item(cart_item)
		
# 		request.session['cart'] = cart.to_dict()

# 		request.session['cart_update_popup'] = True

# 		return redirect('web:product-detail', 
# 						url_name=product.url_name)


# class CartDeleteItemAction(BaseView):
# 	def post(self, request):
# 		product_id = request.POST.get('product_id')

# 		cart = SessionCartManager(request)
# 		cart.remove_item(int(product_id))

# 		request.session['cart'] = cart.to_dict()

# 		return redirect('web:cart')

