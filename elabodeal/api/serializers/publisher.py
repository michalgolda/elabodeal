from rest_framework import serializers
from elabodeal.models import Publisher


class CreatePublisherRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=Publisher.MAX_FIRST_NAME_LENGTH,
        min_length=4
    )
    last_name = serializers.CharField(
        max_length=Publisher.MAX_LAST_NAME_LENGTH,
        min_length=4
    )
    swift = serializers.CharField(
        max_length=Publisher.MAX_SWIFT_LENGHT,
        min_length=Publisher.MAX_SWIFT_LENGHT
    )
    account_number = serializers.CharField(
        max_length=Publisher.MAX_ACCOUNT_NUMBER_LENGTH,
        min_length=Publisher.MAX_ACCOUNT_NUMBER_LENGTH
    )