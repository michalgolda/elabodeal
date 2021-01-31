from rest_framework import serializers


class ResendConfirmEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()