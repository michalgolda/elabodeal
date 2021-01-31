from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdatePublisherSettingsRequestSerializer
from elabodeal.api.interactors import UpdatePublisherSettingsInteractor
from elabodeal.api.repositories import PublisherRepository


class UpdatePublisherSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdatePublisherSettingsRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        publisher_repository = PublisherRepository()

        with UpdatePublisherSettingsInteractor(
            publisher_repo=publisher_repository
        ) as interactor:
            interactor.execute(
                request.user,
                serializer.data
            )

        return self.respond(status=200)

        