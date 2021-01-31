from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdateUserSettingsRequestSerializer
from elabodeal.api.interactors import UpdateUserSettingsInteractor
from elabodeal.api.repositories import UserRepository


class UpdateUserSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdateUserSettingsRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        user_repository = UserRepository()

        with UpdateUserSettingsInteractor(
            user_repo=user_repository
        ) as interactor:
            interactor.execute(
                request.user,
                serializer.data
            )

        return self.respond(status=200)

        