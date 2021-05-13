from rest_framework import serializers
from elabodeal.models import ProductPremiere


class ProductPremiereSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductPremiere
		fields = '__all__'