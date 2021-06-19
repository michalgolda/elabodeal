from django.utils import timezone

from rest_framework import serializers
from elabodeal.models import (
	User,
	Publisher,
	VerificationCode
)


class UpdateUserSettingsRequestSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=User.MAX_USERNAME_LENGTH)

	def validate_username(self, value):
		existing_user = User.objects.filter(username=value).first()

		if existing_user:
			raise serializers.ValidationError(
				'The user which has same username is already exist'
			)

		return value


class UpdatePublisherSettingsRequestSerializer(serializers.Serializer):
	first_name = serializers.CharField(max_length=Publisher.MAX_FIRST_NAME_LENGTH)
	last_name = serializers.CharField(max_length=Publisher.MAX_LAST_NAME_LENGTH)
	account_number = serializers.CharField(max_length=Publisher.MAX_ACCOUNT_NUMBER_LENGTH)
	swift = serializers.CharField(max_length=Publisher.MAX_SWIFT_LENGHT)


class ChangeEmailRequestSerializer(serializers.Serializer):
	email = serializers.EmailField()

	def validate_email(self, value):
		existing_user = User.objects.filter(email=value).first()

		if existing_user:
			raise serializers.ValidationError('This email is already exist')

		return value


class ConfirmEmailChangeRequestSerializer(serializers.Serializer):
	email = serializers.EmailField()
	code = serializers.CharField(
		min_length=VerificationCode.MAX_CODE_LENGTH,
		max_length=VerificationCode.MAX_CODE_LENGTH
	)

	def validate(self, data):
		email = data.get('email')
		code = data.get('code')

		current_datetime = timezone.now()

		existing_code = VerificationCode.objects.filter(email=email).first()

		if not existing_code:
			raise serializers.ValidationError({
				'email': 'The verification code by that email does not exist'
			})

		if current_datetime > existing_code.expiration_at:
			raise serializers.ValidationError({
				'code': 'The verification code is expired'
			})

		if code != existing_code.code:
			raise serializers.ValidationError({
				'code': 'The verification is invalid'
			})

		del data['code']

		return data


