from elabodeal.models import VerificationCode
from elabodeal.api.repositories import Repository


class VerificationCodeRepository(Repository):
    def add(self, *args, **kwargs):
        return VerificationCode.objects.create_code(*args, **kwargs)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())

    def _query_filter(self, *args, **kwargs):
        return VerificationCode.objects.filter(*args, **kwargs)