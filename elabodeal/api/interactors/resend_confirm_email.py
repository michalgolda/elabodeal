from django.utils import timezone

from elabodeal.emails import ConfirmNewUserEmail
from elabodeal.models import VerificationCode, User
from elabodeal.celery.tasks import send_email

from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class ResendConfirmEmailInteractor(Interactor):
    def __init__(self, user_repo: object, code_repo: object):
        self.user_repo = user_repo
        self.code_repo = code_repo

    def execute(self, email: str) -> None:
        existing_user = self.user_repo.find_by_email(email)
        if not existing_user:
            raise ErrorRegistry.RESEND_CONFIRM_EMAIL(
                f'Not found user for that {email} email address'
            )

        existing_code = self.code_repo.find_by_email(email)
        if existing_code:
            self.code_repo.delete(existing_code)

        new_verification_code = VerificationCode.objects.create_code(
            email=email
        )
        
        self.code_repo.save( new_verification_code )

        confirm_new_user_email = ConfirmNewUserEmail(
            to=email,
            context=dict(
                code=new_verification_code.code
            )
        ) 

        send_email.delay(
            email=confirm_new_user_email.asdict()
        )