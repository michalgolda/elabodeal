from django.utils import timezone

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ConfirmEmailRequestSerializer
from elabodeal.api.interactors import ConfirmEmailInteractor


class ConfirmEmailEndpoint(Endpoint):
    def post(self, request):
        serializer = ConfirmEmailRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        with ConfirmEmailInteractor() as interactor:
            interactor.execute(**serializer.data)       

        return self.respond(status=200)

        