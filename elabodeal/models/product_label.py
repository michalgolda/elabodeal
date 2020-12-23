from django.db import models

                              
class ProductLabel(models.Model):
	name = models.CharField(max_length=25)
	color = models.CharField(max_length=6, default='#FF9F1C')