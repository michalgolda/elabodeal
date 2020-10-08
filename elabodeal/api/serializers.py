from rest_framework import serializers


class NewPaymentIntentSerializer(serializers.Serializer):
	email = serializers.EmailField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	phone_number = serializers.RegexField(regex=r'^\+?1?\d{9,15}$')


class ShareCartSerializer(serializers.Serializer):
	title = serializers.CharField()
	description = serializers.CharField()


class ProductUpdateSerializer(serializers.Serializer):
	title = serializers.CharField()
	author = serializers.CharField()