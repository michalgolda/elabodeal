from rest_framework import serializers
from elabodeal.models import User


class UpdateUserSettingsRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)

    def validate_username(self, username: str) -> str:
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            raise serializers.ValidationError(
                'This username is already taken'
            )

        return username

    def validate_email(self, email: str) -> str:
        existing_user = User.objects.filter(email=email).first()
        if existing_user:
            raise serializers.ValidationError(
                'This email is already taken'
            )

        return email