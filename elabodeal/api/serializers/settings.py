from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers

from elabodeal.models import (
	User,
	Publisher,
	VerificationCode
)


class UpdateUserSettingsRequestSerializer(serializers.Serializer):
	username = serializers.CharField(
		default=None,
		max_length=User.MAX_USERNAME_LENGTH
	)
	newsletter = serializers.BooleanField(
		allow_null=True, 
		default=None
	)

	def validate_username(self, value):
		existing_user = User.objects.filter(username=value).first()

		if existing_user:
			raise serializers.ValidationError(
				_('Podana nazwa użytkownika jest już w użyciu')
			)

		return value


class UpdatePublisherSettingsRequestSerializer(serializers.Serializer):
	first_name = serializers.CharField(
		default=None,
		max_length=Publisher.MAX_FIRST_NAME_LENGTH
	)
	last_name = serializers.CharField(
		default=None,
		max_length=Publisher.MAX_LAST_NAME_LENGTH
	)
	account_number = serializers.CharField(
		default=None,
		max_length=Publisher.MAX_ACCOUNT_NUMBER_LENGTH
	)
	swift = serializers.CharField(
		default=None,
		max_length=Publisher.MAX_SWIFT_LENGHT
	)


class ChangeEmailRequestSerializer(serializers.Serializer):
	email = serializers.EmailField()

	def validate_email(self, value):
		existing_user = User.objects.filter(email=value).first()

		if existing_user:
			raise serializers.ValidationError(
				_('Podany adres email jest już w użyciu')
			)

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

		existing_code = VerificationCode.objects.filter(email=email).last()

		if not existing_code:
			raise serializers.ValidationError({
				'email': _(
					'Nie znaleziono kodu weryfikacyjnego',
					'przypisanego do podanego adresu email'
				)
			})

		if current_datetime > existing_code.expiration_at:
			raise serializers.ValidationError({
				'code': _('Podany kod weryfikacyjny jest nieaktwyny')
			})

		if code != existing_code.code:
			raise serializers.ValidationError({
				'code': _('Podany kod weryfikacyjny jest błędny')
			})

		del data['code']

		return data


class ChangePasswordRequestSerializer(serializers.Serializer):
	new_password = serializers.CharField()
	current_password = serializers.CharField()
	
	def validate(self, data):
		new_password = data.get('new_password')
		current_password = data.get('current_password')

		current_password_is_valid = check_password(
			current_password,
			self.instance.password
		)

		if not current_password_is_valid:
			raise serializers.ValidationError({
				'current_password': _('Podane hasło jest błędne')
			})

		try:
			validate_password(new_password)
		except DjangoValidationError as e:
			raise serializers.ValidationError({
				'new_password': list(e.messages)
			})

		del data['current_password']

		return data

