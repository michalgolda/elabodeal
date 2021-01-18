from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdatePublisherSettingsSerializer

from elabodeal.models import Publisher


class UpdatePublisherSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdatePublisherSettingsSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        publisher = request.user.publisher
        options = serializer.data

        Publisher.objects.update_settings(publisher, options)

        return self.respond(status=200)

        