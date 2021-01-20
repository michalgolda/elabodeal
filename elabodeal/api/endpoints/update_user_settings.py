from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import UpdateUserSettingsSerializer

from elabodeal.models import User


class UpdateUserSettingsEndpoint(Endpoint):
    def put(self, request):
        serializer = UpdateUserSettingsSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        user = request.user
        options = serializer.data

        User.objects.update_settings(user, options)

        return self.respond(status=200)

        