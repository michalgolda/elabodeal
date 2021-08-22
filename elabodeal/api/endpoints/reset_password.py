from elabodeal.api.endpoints import Endpoint
from elabodeal.api.interactors import (
    EndResetPasswordFlowInteractor,
    StartResetPasswordFlowInteractor
)
from elabodeal.api.serializers import (
    EndResetPasswordFlowRequestSerializer,
    StartResetPasswordFlowRequestSerializer
)
from elabodeal.api.repositories import (
    UserRepository,
    VerificationCodeRepository
)


class ResetPasswordFlowEndpoint(Endpoint):
    permission_classes = []
 
    def post(self, request):
        serialized_request = StartResetPasswordFlowRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        verification_code_repo = VerificationCodeRepository()

        interactor = StartResetPasswordFlowInteractor(
            verification_code_repo=verification_code_repo
        )
        interactor.execute(**serialized_request.validated_data)

        return self.respond(status=201)

    def put(self, request):
        serialized_request = EndResetPasswordFlowRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        user_repo = UserRepository()
        verification_code_repo = VerificationCodeRepository()

        interactor = EndResetPasswordFlowInteractor(
            user_repo=user_repo,
            verification_code_repo=verification_code_repo
        )
        interactor.execute(**serialized_request.validated_data)

        return self.respond(status=200)