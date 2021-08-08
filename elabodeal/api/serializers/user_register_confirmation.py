from rest_framework import serializers


class ResendUserRegisterConfirmationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()