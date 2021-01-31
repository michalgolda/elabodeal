from rest_framework import serializers


class UpdatePublisherSettingsRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    account_number = serializers.CharField()
    swift = serializers.CharField()
    sell_notification = serializers.BooleanField()