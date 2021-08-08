from django.db import models


class PurchasedProduct(models.Model):
	user = models.ForeignKey('elabodeal.User', on_delete=models.CASCADE)
	product = models.ForeignKey('elabodeal.Product', on_delete=models.CASCADE)
	rating = models.FloatField(default=0)
	has_rating = models.BooleanField(default=False)
	purchased_at = models.DateTimeField(auto_now_add=True)