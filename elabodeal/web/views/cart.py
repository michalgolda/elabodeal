from django.conf import settings
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from elabodeal.models import Product
from elabodeal.web.views import BaseView
from elabodeal.utils import CartSessionManager


class CartView(BaseView):
	def get(self, request):
		session = request.session
		
		cart_manager = CartSessionManager(session)

		cart_manager_as_dict = cart_manager.asdict

		products = cart_manager_as_dict['products']

		context = {
			'application_data': {
				'products': products
			}
		}

		return self.respond('cart.html', request, context)


def required_checkout_session(method):
	def wrapper(request, *args, **kwargs):
		checkout_session = request.session.get('checkout_session')

		if not checkout_session: return redirect('web:index')

		return method(request, *args, **kwargs)
	return wrapper


def validate_checkout_session(method):
	def wrapper(request, *args, **kwargs):
		cart = request.session.get('cart')

		if not cart: return redirect('web:index')

		checkout_session = request.session.get('checkout_session')

		if checkout_session.get('cid') != cart.get('id'):
			return redirect('web:index')

		return method(request, *args, **kwargs)
	return wrapper


class CartCheckoutView(BaseView):

	def get_summary_products(self, request):
		session = request.session

		cart_manager = CartSessionManager(session)

		summary_products = []
		cart_products = cart_manager.selected_products

		for cart_product in cart_products:
			product = Product.objects.filter(id=cart_product.id).first()

			summary_products.append({
				'title': product.title,
				'author': product.author,
				'price': float(product.price)
			})

		return summary_products

	def get_summary_total_price(self, request):
		session = request.session

		cart_manager = CartSessionManager(session)

		summary_total_price = cart_manager.total_price_of_selected_products

		return summary_total_price

	def get_user(self, request):
		user = request.user
		user_is_anonymous = user.is_anonymous

		if user_is_anonymous: return {}

		user_email = user.email

		return {
			'email': user_email
		}

	def get_checkout_session(self, request):
		return request.session.get('checkout_session')

	def get_context(self, request):
		return {
			'application_data': {
				'user': self.get_user(request),
				'checkout_session': self.get_checkout_session(request),
				'summary_products': self.get_summary_products(request),
				'summary_total_price': self.get_summary_total_price(request),
				'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
			}
		}

	@method_decorator([
		required_checkout_session,
		validate_checkout_session
	])
	def get(self, request):
		context = self.get_context(request)

		return self.respond('cart-checkout.html', request, context)
