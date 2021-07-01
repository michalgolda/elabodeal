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

    error = {}
    error['type'] = type(exc).__name__
    error['message'] = response.data.get('detail')

    if error['type'] == 'ValidationError':
        error['message'] = 'Request body data is invalid.'
        error['details'] = response.data

    response.data = {}
    response.data['error'] = error

    return response

