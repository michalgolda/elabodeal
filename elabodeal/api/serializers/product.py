from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from elabodeal.models import Product, File

from .file import FileSerializer
from .product_language import ProductLanguageSerializer


class ProductSerializer(serializers.ModelSerializer):
	other_images = FileSerializer(many=True, read_only=True)
	files = FileSerializer(many=True, read_only=True)
	cover_img = FileSerializer(read_only=True)
	language = ProductLanguageSerializer(read_only=True)

	class Meta:
		model = Product
		fields = '__all__'


class CreateProductRequestSerializer(serializers.Serializer):
	product_group_id = serializers.UUIDField(default=None)
	category_id = serializers.UUIDField()
	product_language_id = serializers.UUIDField()
	title = serializers.CharField(
		max_length=Product.MAX_TITLE_LENGTH
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
	age_category = serializers.ChoiceField(
		choices=Product.AgeCategory.choices
	)
	cover_img = serializers.ImageField()
	other_images = serializers.ListField(
		child=serializers.ImageField(),
		default=None
	)
	files = serializers.ListField(
		child=serializers.FileField(
			validators=[
				FileExtensionValidator(
					allowed_extensions=[
						ext[0] for ext in File.Extension.choices[2:5]
					]
				)
			]
		),
		min_length=1,
		max_length=3
	)