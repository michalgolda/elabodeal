from rest_framework import serializers


class UpdateCheckoutSessionRequestSerializer(serializers.Serializer):
	first_name = serializers.CharField(min_length=4)
	last_name = serializers.CharField(min_length=4)
	email = serializers.EmailField()