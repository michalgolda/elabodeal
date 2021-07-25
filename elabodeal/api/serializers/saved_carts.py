from rest_framework import serializers


class SaveCartRequestSerializer(serializers.Serializer):
	title = serializers.CharField(min_length=10)
	description = serializers.CharField(max_length=1500)