from rest_framework import serializers


class ResendEmailVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()