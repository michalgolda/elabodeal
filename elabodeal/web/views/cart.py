
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

	def calculate_total_price(self, products):
		total_price = 0.00

		for product in products:
			total_price += product['price']

		total_price = '{0:.2f}'.format(round(total_price, 2))

		return total_price

	def post(self, request):
		action_type = request.POST.get('action_type')

		if not 'cart' in request.session:
			request.session['cart'] = {
				'products': [],
				'item_count': 0,
				'total_price': 0.00
			}

		cart = request.session['cart']

		if action_type == 'add-product':
			product_id = int(request.POST.get('product_id'))

			product = Product.objects.filter(id=product_id).first()

			# Check if product does exists in cart
			for cart_item in cart['products']:
				if cart_item['id'] == product_id:
					return redirect('web:product-detail', url_name=product.url_name)

			cart['products'].append({'id': product_id, 'price': float(product.price)})
			cart['total_price'] = self.calculate_total_price(cart['products'])
			cart['item_count'] += 1

			request.session['cart'] = cart

			context = {
				'success_msg': True,
				'products': self.get_cart_products(request)
			}
			return self.respond('cart.html', request, context)

		if action_type == 'delete-product':
			product_id = int(request.POST.get('product_id'))

			for product in cart['products']:
				if product['id'] == product_id:
					cart['products'].remove(product)

			cart['total_price'] = self.calculate_total_price(cart['products'])
			cart['item_count'] -= 1

			request.session['cart'] = cart

		if action_type == 'save-cart':
			cart_title = request.POST.get('title')
			cart_description = request.POST.get('description')

			cart = Cart()
			cart.user = request.user
			cart.title = cart_title
			cart.description = cart_description
			cart.save()

			for obj in request.session['cart']['products']:
				product = Product.objects.filter(id=obj['id']).first()

				cart_item = CartItem()
				cart_item.cart = cart
				cart_item.product = product
				cart_item.save()

			return redirect('web:saved-carts')

		return redirect('web:cart')

	def get(self, request):
		context = {
			'products': self.get_cart_products(request)
		}
		return self.respond('cart.html', request, context)