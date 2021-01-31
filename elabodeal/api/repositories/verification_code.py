from elabodeal.models import VerificationCode
from elabodeal.api.repositories import Repository


class VerificationCodeRepository(Repository):
    def get(self, id: int) -> VerificationCode:
        return VerificationCode.objects.filter(id=id).first()

    def delete(self, code: VerificationCode) -> None:
        code.delete()

    def save(self, code: VerificationCode) -> VerificationCode:
        code.save()

        return code

    def find_by_email(self, email: str) -> VerificationCode:
        return VerificationCode.objects.filter(email=email).first()