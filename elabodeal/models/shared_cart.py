import uuid
import random
import string

from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _


class SharedCartManager(models.Manager):
	def create_shared_cart(self, cart):
		code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
		shared_cart = self.model(
			code=code,
			cart=cart
		)
		shared_cart.save()

		return shared_cart


class SharedCart(models.Model):
	MAX_CODE_LENGTH = 6
	MIN_CODE_LENGTH = 6

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)	
	cart = models.ForeignKey(
		'elabodeal.Cart', 
		on_delete=models.CASCADE
	)
	code = models.CharField(max_length=MAX_CODE_LENGTH)
	created_at = models.DateTimeField(auto_now_add=True)

	objects = SharedCartManager()

	class Meta:
		verbose_name = _('Udostępniony koszyk')
		verbose_name_plural = _('Udostępnione koszyki')

	@property
	def share_url_path(self):
		return reverse('web:shared-cart', args=[self.code])

	def __str__(self):
		return str(self.id)