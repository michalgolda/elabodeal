from rest_framework import serializers


class UpdateCartRequestSerializer(serializers.Serializer):
	product_id = serializers.UUIDField()


class AddProductToCartRequestSerializer(UpdateCartRequestSerializer):
	clear = serializers.BooleanField(default=False)