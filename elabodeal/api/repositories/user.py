from elabodeal.models import User
from elabodeal.api.repositories import Repository


class UserRepository(Repository):
    def add(self, *args, **kwargs):
        return User.objects.create_user(*args, **kwargs)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())
    
    def save(self, user):
        user.save()

        return user

    def _query_filter(self, *args, **kwargs):
        return User.objects.filter(*args, **kwargs)