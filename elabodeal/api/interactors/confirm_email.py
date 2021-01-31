from dataclasses import dataclass

from django.utils import timezone

from elabodeal.models import VerificationCode, User

from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class ConfirmEmailInteractor(Interactor):
    def __init__(self, user_repo: object, code_repo: object):
        self.user_repo = user_repo
        self.code_repo = code_repo

    def execute(self, email: str, code: str) -> None:
        existing_user = self.user_repo.find_by_email(email)
        if not existing_user:
            raise ErrorRegistry.CONFIRM_EMAIL('Not found candidate for email confirmation')
        
        existing_code = self.code_repo.find_by_email(email)
        if not existing_code:
            raise ErrorRegistry.CONFIRM_EMAIL(f'Not found existing verification code for {email}')

        if existing_code.code != code:
            raise ErrorRegistry.CONFIRM_EMAIL('Verification code is invalid')

        current_datetime = timezone.now()
        expiration_datetime = existing_code.expiration_at

        if current_datetime > expiration_datetime:
            raise ErrorRegistry.CONFIRM_EMAIL('Verification code is expired')
    
        self.code_repo.delete(existing_code)

        existing_user.email_verified = True
        existing_user.email_verified_at = timezone.now()
        
        self.user_repo.save(existing_user)
        
