import uuid
from django.db import models
from django.utils.translation import gettext as _


class Cart(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)

	user = models.ForeignKey(
		'elabodeal.User', 
		on_delete=models.CASCADE
	)

	products = models.ManyToManyField('elabodeal.Product')

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('Koszyk')
		verbose_name_plural = _('Koszyki')

	@property
	def products_count(self):
		return self.products.count()

	@property
	def total_price(self):
		total_price = 0.00

		for product in self.products.all():
			total_price += float(product.price)

		return '{0:.2f}'.format(round(total_price, 2))

	def __str__(self):
		return str(self.id)