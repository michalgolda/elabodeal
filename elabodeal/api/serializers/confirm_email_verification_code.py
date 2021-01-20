from django.utils import timezone
from rest_framework import serializers

from elabodeal.models import VerificationCode


class ConfirmEmailVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        if len(value) > 6 or len(value) < 6:
            raise serializers.ValidationError(
                'Verification code is invalid'
            )

        return value