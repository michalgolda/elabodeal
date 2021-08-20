from rest_framework import serializers
from elabodeal.models import Publisher
from django.utils.translation import gettext as _


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


class FollowPublisherRequestSerializer(serializers.Serializer):
    publisher_id = serializers.UUIDField()

    def validate_publisher_id(self, publisher_id):
        existing_publisher = Publisher.objects.filter(id=publisher_id).first()

        if not existing_publisher:
            raise serializers.ValidationError(
                _('Wydawca o podanym identyfikatorze nie istnieje.')
            )

        return publisher_id