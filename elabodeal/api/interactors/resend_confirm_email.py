from django.utils import timezone

from elabodeal.emails import ConfirmChangeEmail
from elabodeal.models import VerificationCode, User
from elabodeal.celery.tasks import send_email

from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class ResendConfirmEmailInteractor(Interactor):
    def execute(self, email: str) -> None:
        existing_user = User.objects.filter(email=email).first()
        if not existing_user:
            raise ErrorRegistry.RESEND_CONFIRM_EMAIL(
                f'Not found user for that {email} email address'
            )

        existing_code = VerificationCode.objects.filter(email=email).first()
        if existing_code:
            existing_code.delete()

        new_verification_code = VerificationCode.objects.create_code(
            email=email
        )

        confirm_change_email = ConfirmChangeEmail(
            to=email,
            context=dict(
                code=new_verification_code.code
            )
        ) 

        send_email.delay(
            email=confirm_change_email.asdict()
        )