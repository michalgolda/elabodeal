
from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.models import Product, Cart, CartItem


class CartView(BaseView):
	def get_cart_products(self, request):
		products = []
		
		if 'cart' in request.session:
			for p in request.session['cart']['products']:
				product = Product.objects.filter(id=p['id']).first()
				products.append(product)

		return products

	def calculate_total_price(self, request):
		total_price = 0.00

		for p in request.session['cart']['products']:
			total_price += p['price']

		total_price = '{0:.2f}'.format(round(total_price, 2))

		return total_price

	def post(self, request):
		if not 'cart' in request.session:
			request.session['cart'] = {
				'products': [],
				'item_count': 0,
				'total_price': 0.00
			}

		action_type = request.POST.get('action_type')
		
		if action_type == 'add-product-to-cart':
			product_id = int(request.POST.get('product_id'))
			product_price = float(request.POST.get('product_price'))

			cart = request.session['cart']

			cart['products'].append({'id': product_id, 'price': product_price})
			cart['total_price'] = self.calculate_total_price(request)
			cart['item_count'] += 1

			request.session['cart'] = cart

			context = {
				'show_info': True,
				'products': self.get_cart_products(request)
			}
			return self.respond('cart.html', request, context)

		elif action_type == 'delete-product-from-cart':
			product_id = int(request.POST.get('product_id'))

			cart = request.session['cart']

			for p in cart['products']:
				if p['id'] == product_id:
					cart['products'].remove(p)

			cart['total_price'] = self.calculate_total_price(request)
			cart['item_count'] -= 1

			request.session['cart'] = cart

			return redirect('web:cart')
		elif action_type == 'save-cart':
			cart_title = request.POST.get('title')
			cart_description = request.POST.get('description')

			cart = Cart()
			cart.user = request.user
			cart.title = cart_title
			cart.description = cart_description
			cart.save()

			for p in request.session['cart']['products']:
				product = Product.objects.filter(id=p['id']).first()
				cart_item = CartItem()
				cart_item.cart = cart
				cart_item.product = product
				cart_item.save()


			return redirect('web:my-carts')

	def get(self, request):
		context = {
			'products': self.get_cart_products(request)
		}
		return self.respond('cart.html', request, context)