from rest_framework import serializers
from elabodeal.models import ProductGroup


class ProductGroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductGroup
		fields = '__all__'


class CreateProductGroupRequestSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=ProductGroup.MAX_NAME_LENGTH)