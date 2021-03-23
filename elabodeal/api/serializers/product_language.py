from rest_framework import serializers
from elabodeal.models import ProductLanguage


class ProductLanguageSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductLanguage
		fields = '__all__'