from django.db import models


class CartItem(models.Model):
	product = models.ForeignKey('elabodeal.Product', 
						 		on_delete=models.CASCADE)