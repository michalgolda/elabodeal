import uuid
import json

from itertools import chain

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from elabodeal.celery.tasks import clear_product_files


class Product(models.Model):

	class AgeCategory(models.IntegerChoices):
		PEGI_3 = 3
		PEGI_7 = 7
		PEGI_12 = 12
		PEGI_16 = 16
		PEGI_18 = 18

	MAX_TITLE_LENGTH = 50
	MIN_TITLE_LENGTH = 10
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
	language = models.ForeignKey(
		'elabodeal.ProductLanguage',
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
	other_images = models.ManyToManyField(
		'elabodeal.File',
		related_name='other_images'
	)
	files = models.ManyToManyField('elabodeal.File')
	age_category = models.IntegerField(choices=AgeCategory.choices)
	average_rating = models.FloatField(default=0)
	rating_count = models.IntegerField(default=0)
	
	premiere = models.OneToOneField(
		'elabodeal.ProductPremiere',
		on_delete=models.CASCADE,
		null=True
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@property
	def filled_stars(self):
		return range(int(self.average_rating))

	@property
	def empty_stars(self):
		return range(int(5 - self.average_rating))


@receiver(pre_delete, sender=Product)
def clear_product_files_handler(sender, instance, *args, **kwargs):
	other_images_queryset = instance.other_images.all()
	files_queryset = instance.files.all()
	cover_img = instance.cover_img

	file_objects = list(chain(other_images_queryset, files_queryset))
	file_objects.append(cover_img)

	file_list = []
	for file in file_objects:
		file_id = str(file.id)
		file_extension = file.extension
		file_name = f'{file_id}.{file_extension}'

		file_list.append({'id': file_id, 'name': file_name})

	clear_product_files.delay(json.dumps(file_list))

