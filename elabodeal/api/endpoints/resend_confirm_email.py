from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ResendConfirmEmailRequestSerializer
from elabodeal.api.interactors import ResendConfirmEmailInteractor
from elabodeal.api.repositories import UserRepository, VerificationCodeRepository


class ResendConfirmEmailEndpoint(Endpoint):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = ResendConfirmEmailRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        code_repository = VerificationCodeRepository()
        user_repository = UserRepository()

        with ResendConfirmEmailInteractor(
            user_repo=user_repository,
            code_repo=code_repository
        ) as interactor:
            interactor.execute(**serializer.data)

        return self.respond(status=200)