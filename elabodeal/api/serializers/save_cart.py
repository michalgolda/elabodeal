from rest_framework import serializers


class SaveCartRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()