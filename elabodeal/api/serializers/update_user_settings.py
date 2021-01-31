from rest_framework import serializers


class UpdateUserSettingsRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)