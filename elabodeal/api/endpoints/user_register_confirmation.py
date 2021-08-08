from django.utils import timezone

from elabodeal.api.repositories import (
    UserRepository, 
    VerificationCodeRepository
)
from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import (
    UserRegisterConfirmationInteractor,
    ResendUserRegisterConfirmationInteractor
)
from elabodeal.api.serializers import (
    ConfirmEmailChangeRequestSerializer,
    ResendUserRegisterConfirmationRequestSerializer
)


class UserRegisterConfirmationEndpoint(Endpoint):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serialized_request = ConfirmEmailChangeRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        user_repo = UserRepository()
        verification_code_repo = VerificationCodeRepository()

        interactor = UserRegisterConfirmationInteractor(
            user_repo=user_repo,
            verification_code_repo=verification_code_repo
        )
        interactor.execute(**serialized_request.validated_data)

        return self.respond(status=200)

        
class ResendUserRegisterConfirmationEndpoint(Endpoint):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serialized_request = ResendUserRegisterConfirmationRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        verification_code_repo = VerificationCodeRepository()

        interactor = ResendUserRegisterConfirmationInteractor(
            verification_code_repo=verification_code_repo
        )
        interactor.execute(**serialized_request.validated_data)

        return self.respond(status=200)