import stripe
import json

from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from elabodeal.web.views import BaseView, BaseAjaxView
from elabodeal.web.forms import DeliveryForm
from elabodeal.models import Product, Cart, CartItem
from elabodeal.utils import SessionCartManager


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


class CartAddItemAction(BaseView):
	def post(self, request):
		product_id = request.POST.get('product_id')
		
		product = Product.objects.filter(id=int(product_id)).first()
		if not product:
			return redirect('web:index')

		cart = SessionCartManager(request)

		for item in cart.items:
			if item.id == product.id:
				return redirect('web:product-detail', 
								url_name=product.url_name)

		cart_item = cart.Item(id=product.id, 
							  price=float(product.price))
		cart.add_item(cart_item)
		
		request.session['cart'] = cart.to_dict()

		request.session['cart_update_popup'] = True

		return redirect('web:product-detail', 
						url_name=product.url_name)


class CartDeleteItemAction(BaseView):
	def post(self, request):
		product_id = request.POST.get('product_id')

		cart = SessionCartManager(request)
		cart.remove_item(int(product_id))

		request.session['cart'] = cart.to_dict()

		return redirect('web:cart')


class CartSaveAjaxView(BaseAjaxView):
	auth_required = True

	def post(self, request):
		title = request.POST.get('title')
		description = request.POST.get('description')

		if not title or not description:
			return self.respond(message='BadRequest',
								status=400)

		cart = SessionCartManager(request)
		
		user = request.user

		saved_cart = Cart(user=user,
						  title=title,
						  description=description)
		saved_cart.save()
		
		for item in cart.items:
			product = Product.objects.filter(id=item.id).first()

			saved_cart.items.create(product=product)

		return self.respond(message="Success",
							status=201)

