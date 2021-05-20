from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler as rest_framework_exception_handler


class LogicException(APIException):
    type = 'logic_error'

    def __init__(self, message: str):
        super().__init__(detail=message)


class ResourceIsAlreadyExists(LogicException):
    status_code = 400
    type = 'resource_is_already_exists'


class ResourceDoesNotExists(LogicException):
    status_code = 404
    type = 'resource_does_not_exists'


def exception_handler(exc, context):
    response = rest_framework_exception_handler(exc, context)

    if isinstance(exc, LogicException):
        response.data['status_code'] = exc.status_code
        response.data['type'] = exc.type

    return response