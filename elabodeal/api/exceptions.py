from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler as rest_framework_exception_handler


class LogicException(APIException):
    type = 'logic_error'

    def __init__(self, message: str):
        super().__init__(detail=message)


class ConfirmEmailException(LogicException):
    status_code = 400
    type = 'email_confirmation_error'


class ResendConfirmEmailException(LogicException):
    status_code = 400
    type = 'resend_confirmation_email_error'


class UpdatePublisherSettingsException(LogicException):
    status_code = 400
    type = 'update_publisher_settings_error'


class UpdateUserSettingsException(LogicException):
    status_code = 400
    type = 'update_user_settings_error'


class ErrorRegistry:
    LOGIC = LogicException
    CONFIRM_EMAIL = ConfirmEmailException
    RESEND_CONFIRM_EMAIL = ResendConfirmEmailException
    UPDATE_PUBLISHER_SETTINGS = UpdatePublisherSettingsException
    UPDATE_USER_SETTINGS = UpdateUserSettingsException


def exception_handler(exc, context):
    response = rest_framework_exception_handler(exc, context)

    if isinstance(exc, LogicException):
        response.data['status_code'] = exc.status_code
        response.data['type'] = exc.type

    return response