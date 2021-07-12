from rest_framework import serializers


class UpdateCartRequestSerializer(serializers.Serializer):
	product_id = serializers.UUIDField()


class SaveCartRequestSerializer(serializers.Serializer):
	title = serializers.CharField(min_length=10)
	description = serializers.CharField(max_length=200)