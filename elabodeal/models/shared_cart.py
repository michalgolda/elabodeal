import random
import string

from django.db import models
from django.shortcuts import reverse


class SharedCartManager(models.Manager):
	def create_share(self, cart):
		shared_cart = self.model.objects.filter(cart=cart).first()

		if not shared_cart:			
				code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

				shared_cart = self.model.objects.create(code=code, 
														cart=cart)

		return shared_cart


class SharedCart(models.Model):
	code = models.CharField(max_length=6)
	cart = models.ForeignKey('elabodeal.Cart', 
					  		 on_delete=models.CASCADE)

	shared_at = models.DateTimeField(auto_now_add=True)

	objects = SharedCartManager()

	@property
	def url(self):
		return reverse('web:shared-cart-detail', args=[self.code])
