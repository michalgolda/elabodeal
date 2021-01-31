from dataclasses import dataclass

from django.utils import timezone

from elabodeal.models import VerificationCode, User

from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class ConfirmEmailInteractor(Interactor):
    def execute(self, email: str, code: str) -> None:
        existing_user = User.objects.filter(email=email).first()
        if not existing_user:
            raise ErrorRegistry.CONFIRM_EMAIL('Not found candidate for email confirmation')
        
        existing_code = VerificationCode.objects.filter(email=email).first()
        if not existing_code:
            raise ErrorRegistry.CONFIRM_EMAIL(f'Not found existing verification code for {email}')

        if existing_code.code != code:
            raise ErrorRegistry.CONFIRM_EMAIL('Verification code is invalid')

        current_datetime = timezone.now()
        expiration_datetime = existing_code.expiration_at

        if current_datetime > expiration_datetime:
            raise ErrorRegistry.CONFIRM_EMAIL('Verification code is expired')
    
        existing_code.delete()

        existing_user.email_verified = True
        existing_user.email_verified_at = timezone.now()
        existing_user.save()
        
