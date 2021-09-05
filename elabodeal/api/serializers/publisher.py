from rest_framework import serializers
from elabodeal.models import Publisher
from django.utils.translation import gettext as _

from .file import FileSerializer
from .product import ProductSerializer



class PublisherProfileSerializer(serializers.ModelSerializer):
    banner_img = FileSerializer(read_only=True)
    avatar_img = FileSerializer(read_only=True)
    banner_product = ProductSerializer(read_only=True)

    class Meta:
        model = Publisher
        fields = [
            'bio',
            'banner_img', 
            'avatar_img', 
            'banner_text', 
            'who_you_are',
            'banner_product'
        ]


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


class UpdatePublisherProfileRequestSerializer(serializers.Serializer):
    banner_text = serializers.CharField(
        default=None,
        allow_null=True, 
        max_length=Publisher.MAX_BANNER_TEXT_LENGTH
    )
    banner_product = serializers.UUIDField(
        default=None, 
        allow_null=True
    )
    who_you_are = serializers.CharField(
        default=None,
        allow_null=True,
        max_length=Publisher.MAX_WHO_YOU_ARE_LENGTH
    )
    bio = serializers.CharField(
        default=None,
        allow_null=True,
        max_length=Publisher.MAX_BIO_LENGTH
    )


class UpdatePublisherProfileAvatarImgRequestSerializer(serializers.Serializer):
    avatar_img = serializers.ImageField(
        default=None, 
        allow_null=True
    )


class UpdatePublisherProfileBannerImgRequestSerializer(serializers.Serializer):
    banner_img = serializers.ImageField(
        default=None,
        allow_null=True
    )
