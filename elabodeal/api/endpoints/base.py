from rest_framework.views import APIView
from rest_framework.response import Response


class Endpoint(APIView):
    def respond(self, data=None, status=200, *args, **kwargs):
        return Response(data, status, *args, **kwargs)