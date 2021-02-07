from django.utils import timezone

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ConfirmEmailRequestSerializer
from elabodeal.api.interactors import ConfirmEmailInteractor
from elabodeal.api.repositories import UserRepository, VerificationCodeRepository


class ConfirmEmailEndpoint(Endpoint):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = ConfirmEmailRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        code_repository = VerificationCodeRepository()
        user_repository = UserRepository()

        with ConfirmEmailInteractor(
            user_repo=user_repository,
            code_repo=code_repository
        ) as interactor:
            interactor.execute(**serializer.data)       

        return self.respond(status=200)

        