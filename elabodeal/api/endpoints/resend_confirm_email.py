from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ResendConfirmEmailRequestSerializer
from elabodeal.api.interactors import ResendConfirmEmailInteractor


class ResendConfirmEmailEndpoint(Endpoint):
    def post(self, request):
        serializer = ResendConfirmEmailRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        with ResendConfirmEmailInteractor() as interactor:
            interactor.execute(**serializer.data)

        return self.respond(status=200)