from typing import List
from elabodeal.models import User

from elabodeal.api.repositories import Repository


class UserRepository(Repository):
    def get(self, id: int) -> User:
        return User.objects.filter(id=id).first()

    def delete(self, user: User) -> None:
        user.remove()

    def save(self, user: User) -> User:
        user.save()

        return user

    def find_by_email(self, email: str) -> User:
        return User.objects.filter(email=email).first()