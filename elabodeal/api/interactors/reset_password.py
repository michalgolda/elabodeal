from elabodeal.api.interactors import Interactor
from elabodeal.emails import ResetPasswordRequestEmail


class StartResetPasswordFlowInteractor(Interactor):
    def __init__(self, verification_code_repo):
        self.verification_code_repo = verification_code_repo
    
    def execute(self, email):
        verification_code = self.verification_code_repo.add(email=email)

        reset_password_request_email = ResetPasswordRequestEmail(
            to=email,
            template_context={
                'code': verification_code.code
            }
        )
        reset_password_request_email.send()


class EndResetPasswordFlowInteractor(Interactor):
    def __init__(self, user_repo, verification_code_repo):
        self.user_repo = user_repo
        self.verification_code_repo = verification_code_repo

    def execute(self, email, password):
        user = self.user_repo.get_one_by(email=email)

        user.set_password(password)

        self.user_repo.save(user)

        self.verification_code_repo.delete_by(email=email)