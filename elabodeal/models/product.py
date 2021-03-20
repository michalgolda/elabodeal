import uuid
from django.db import models


class Product(models.Model):

	class AgeCategory(models.IntegerChoices):
		PEGI_3 = 3
		PEGI_7 = 7
		PEGI_12 = 12
		PEGI_16 = 16
		PEGI_18 = 18

	MAX_TITLE_LENGTH = 50
	MAX_DESCRIPTION_LENGTH = 400
	MAX_CONTENTS_LENGTH = 500
	MAX_AUTHOR_LENGTH = 30
	MAX_ISBN_LENGTH = 13
	MAX_PRICE_DIGITS = 10
	PRICE_DECIMALS_PLACES = 2

	id = models.UUIDField(
		primary_key=True, 
		default=uuid.uuid4,
		editable=False 
	)
	publisher = models.ForeignKey(
		'elabodeal.Publisher',
		on_delete=models.CASCADE
	)
	group = models.ForeignKey(
		'elabodeal.ProductGroup',
		on_delete=models.CASCADE
	)
	category = models.ForeignKey(
		'elabodeal.Category',
		on_delete=models.CASCADE
	)
	title = models.CharField(max_length=MAX_TITLE_LENGTH)
	description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
	contents = models.CharField(
		max_length=MAX_CONTENTS_LENGTH,
		null=True,
		blank=True
	)
	author = models.CharField(max_length=MAX_AUTHOR_LENGTH)
	isbn = models.CharField(max_length=MAX_ISBN_LENGTH)
	price = models.DecimalField(
		max_digits=MAX_PRICE_DIGITS, 
		decimal_places=PRICE_DECIMALS_PLACES
	)
	cover_img = models.ForeignKey(
		'elabodeal.File',
		on_delete=models.CASCADE,
		related_name='cover_img'
	)
	other_images = models.ManyToManyField('elabodeal.File'),
	files = models.ManyToManyField('elabodeal.File')
	age_category = models.IntegerField(choices=AgeCategory.choices)
	average_rating = models.FloatField(default=0)
	rating_count = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@property
	def filled_stars(self):
		return range(int(self.average_rating))

	@property
	def empty_stars(self):
		return range(int(5 - self.average_rating))