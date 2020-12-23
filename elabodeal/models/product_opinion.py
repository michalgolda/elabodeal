from django.db import models


class ProductOpinion(models.Model):
	user = models.ForeignKey('elabodeal.User',
					  		 on_delete=models.CASCADE)

	content = models.CharField(max_length=100)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)