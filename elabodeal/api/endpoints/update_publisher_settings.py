from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdatePublisherSettingsRequestSerializer
from elabodeal.api.interactors import UpdatePublisherSettingsInteractor


class UpdatePublisherSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdatePublisherSettingsRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        with UpdatePublisherSettingsInteractor() as interactor:
            interactor.execute(
                request.user,
                serializer.data
            )

        return self.respond(status=200)

        