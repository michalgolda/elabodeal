from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdateUserSettingsRequestSerializer
from elabodeal.api.interactors import UpdateUserSettingsInteractor


class UpdateUserSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdateUserSettingsRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        with UpdateUserSettingsInteractor() as interactor:
            interactor.execute(
                request.user,
                serializer.data
            )

        return self.respond(status=200)

        