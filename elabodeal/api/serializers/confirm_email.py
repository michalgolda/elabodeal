from django.utils import timezone
from rest_framework import serializers

from elabodeal.models import VerificationCode


class ConfirmEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(
        min_length=VerificationCode.MAX_CODE_LENGTH,
        max_length=VerificationCode.MAX_CODE_LENGTH
    )