import uuid
from django.db import models
from django.utils.translation import gettext as _


class PurchasedProduct(models.Model):
	id = models.UUIDField(
		editable=False,
		primary_key=True,
		default=uuid.uuid4
	)
	user = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE)
	product = models.ForeignKey('elabodeal.Product', on_delete=models.CASCADE)
	rating = models.FloatField(default=0)
	has_rating = models.BooleanField(default=False)
	purchased_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _('Kupiony produkt')
		verbose_name_plural = _('Kupione produkty')

	def __str__(self):
		return str(self.id)