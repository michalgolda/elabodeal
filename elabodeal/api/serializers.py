from rest_framework import serializers


class NewPaymentIntentSerailizer(serializers.Serializer):
	email = serializers.EmailField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	phone_number = serializers.RegexField(regex=r'^\+?1?\d{9,15}$')