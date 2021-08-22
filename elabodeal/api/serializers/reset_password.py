from rest_framework import serializers
from django.utils.translation import gettext as _
from elabodeal.models import (
    User,
    VerificationCode
)
from elabodeal.models.verification_code import VerificationCodeValidationError


class StartResetPasswordFlowRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        existing_user = User.objects.filter(email=email).first()

        if not existing_user:
            raise serializers.ValidationError(
                _('Adres email jest błędny lub użytkownik o podanym adresie email nie istnieje.')
            )

        return email


class EndResetPasswordFlowRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(
        max_length=VerificationCode.MAX_CODE_LENGTH,
        min_length=VerificationCode.MAX_CODE_LENGTH
    )
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate_email(self, email):
        existing_user = User.objects.filter(email=email).first()

        if not existing_user:
            raise serializers.ValidationError(
                _('Adres email jest błędny lub użytkownik o podanym adresie email nie istnieje.')
            )

        return email

    def validate(self, data):
        email = data['email']
        code = data['code']

        try:
            VerificationCode.objects.validate(email, code)
        except VerificationCodeValidationError as e:
            raise serializers.ValidationError({
                'code': str(e)
            })

        new_password1 = data['new_password1']
        new_password2 = data['new_password2']

        if new_password1 != new_password2:
            raise serializers.ValidationError({
                'new_password1': _('Podane hasła nie są takie same'),
                'new_password2': _('Podane hasła nie są takie same')
            })

        data['password'] = data['new_password1']

        del data['code']
        del data['new_password1']
        del data['new_password2']

        return data
