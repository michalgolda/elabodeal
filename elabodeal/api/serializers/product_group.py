from rest_framework import serializers
from elabodeal.models import ProductGroup


class ProductGroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductGroup
		fields = '__all__'