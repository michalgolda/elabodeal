from rest_framework import serializers


class UpdateUserSettingsSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField(required=False)