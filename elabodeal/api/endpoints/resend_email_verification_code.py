from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ResendEmailVerificationCodeSerializer

from elabodeal.models import (
    VerificationCode, 
    VerificationCodeException
)


class ResendEmailVerificationCodeEndpoint(Endpoint):
    def post(self, request):
        serializer = ResendEmailVerificationCodeSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']

        try:
            VerificationCode.objects.generate(email)
        except VerificationCodeException:
            return self.respond(status=400)

        return self.respond(status=200)