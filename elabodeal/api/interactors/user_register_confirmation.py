from django.utils import timezone
from elabodeal.api.interactors import Interactor
from elabodeal.emails import UserRegisterConfirmationEmail


class UserRegisterConfirmationInteractor(Interactor):
    def __init__(self, user_repo, verification_code_repo):
        self.user_repo = user_repo
        self.verification_code_repo = verification_code_repo

    def execute(self, email):
        user = self.user_repo.get_one_by(email=email)

        user.email_verified = True
        user.email_verified_at = timezone.now()

        self.user_repo.save(user)

        self.verification_code_repo.delete_by(email=email)


class ResendUserRegisterConfirmationInteractor(Interactor):
    def __init__(self, verification_code_repo):
        self.verification_code_repo = verification_code_repo

    def execute(self, email):
        self.verification_code_repo.delete_by(email=email)

        new_verification_code = self.verification_code_repo.add(
            email=email
        )

        user_register_confirmation_email = UserRegisterConfirmationEmail(
            to=email,
            template_context={
                'code': new_verification_code.code
            }
        )
        user_register_confirmation_email.send()
