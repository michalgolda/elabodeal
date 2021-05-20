import datetime

from django.utils import timezone
from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from elabodeal.models import Product, File

from .file import FileSerializer
from .product_language import ProductLanguageSerializer
from .product_premiere import ProductPremiereSerializer


EBOOK_FILE_EXTENSIONS = [
	ext[0] for ext in File.Extension.choices[2:5]
] 


class ProductSerializer(serializers.ModelSerializer):
	other_images = FileSerializer(many=True, read_only=True)
	files = FileSerializer(many=True, read_only=True)
	cover_img = FileSerializer(read_only=True)
	language = ProductLanguageSerializer(read_only=True)
	premiere = ProductPremiereSerializer(read_only=True)

	class Meta:
		model = Product
		fields = '__all__'


class CreateProductRequestSerializer(serializers.Serializer):
	product_group_id = serializers.UUIDField(default=None)
	category_id = serializers.UUIDField()
	product_language_id = serializers.UUIDField()
	title = serializers.CharField(
		max_length=Product.MAX_TITLE_LENGTH,
		min_length=Product.MIN_TITLE_LENGTH
	)
	description = serializers.CharField(
		max_length=Product.MAX_DESCRIPTION_LENGTH
	)
	contents = serializers.CharField(
		max_length=Product.MAX_CONTENTS_LENGTH,
		allow_null=True
	)
	author = serializers.CharField(
		max_length=Product.MAX_AUTHOR_LENGTH
	)
	isbn = serializers.CharField(
		max_length=Product.MAX_ISBN_LENGTH,
		min_length=Product.MAX_ISBN_LENGTH	
	)
	price = serializers.DecimalField(
		max_digits=Product.MAX_PRICE_DIGITS,
		decimal_places=Product.PRICE_DECIMALS_PLACES
	)
	copies = serializers.IntegerField(
		min_value=0,
		default=0
	)
	published_year = serializers.IntegerField()
	page_count = serializers.IntegerField(min_value=1)
	age_category = serializers.ChoiceField(
		choices=Product.AgeCategory.choices
	)
	cover_img = serializers.ImageField()
	other_images = serializers.ListField(
		child=serializers.ImageField(),
		default=[]
	)
	files = serializers.ListField(
		child=serializers.FileField(
			validators=[
				FileExtensionValidator(
					allowed_extensions=EBOOK_FILE_EXTENSIONS
				)
			]
		),
		min_length=1,
		max_length=3
	)
	premiere_datetime = serializers.DateTimeField()

	def validate_premiere_datetime(self, premiere_datetime):
		current_datetime = timezone.now()
		max_premiere_datetime = current_datetime + datetime.timedelta(days=365)

		if ( premiere_datetime < current_datetime and 
		     premiere_datetime < max_premiere_datetime ):
			raise serializers.ValidationError(
				"Premiere date and time must be in the future and one year forward"
			)

		return premiere_datetime