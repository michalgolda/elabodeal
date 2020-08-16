from django.urls import reverse
from tests.base import WebTestCase

from elabodeal.models import SharedCart, User


class TestSharedCartView(WebTestCase):
	def test_simple(self):
		shared_cart = SharedCart(
			code=SharedCart.generate_code(), 
			title='test', 
			description='test'
		)
		shared_cart.save()

		response = self.client.get(reverse('web:shared-cart', args=[shared_cart.code]))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'shared_cart.html')

	def test_invalid_shared_cart_code(self):
		response = self.client.get(reverse('web:shared-cart', args=['123']), follow=True)

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')