from django.utils import timezone

from elabodeal.api.endpoints import Endpoint
from elabodeal.api.serializers import ConfirmEmailVerificationCodeSerializer

from elabodeal.models import (
    User,
    VerificationCode, 
    VerificationCodeException
)


class ConfirmEmailVerificationCodeEndpoint(Endpoint):
    def post(self, request):
        serializer = ConfirmEmailVerificationCodeSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        code = serializer.data['code']

        try:
            VerificationCode.objects.verify(email, code)
        except VerificationCodeException:
            return self.respond(status=400)

        return self.respond(status=200)

        