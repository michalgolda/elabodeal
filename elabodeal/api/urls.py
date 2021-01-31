from django.urls import path

from elabodeal.api.endpoints import (
    ConfirmEmailEndpoint,
    ResendConfirmEmailEndpoint,
    UpdateUserSettingsEndpoint,
    UpdatePublisherSettingsEndpoint
)

app_name = 'api'

urlpatterns = [
    path(
        'verify/email/',
        ConfirmEmailEndpoint.as_view(),
        name='confirm-email-verification-code'
    ),
    path(
        'verify/email/resend/',
        ResendConfirmEmailEndpoint.as_view(),
        name='resend-email-verification-code'
    ),
    path(
        'users/me/settings/',
        UpdateUserSettingsEndpoint.as_view(),
        name='update-user-settings'
    ),
    path(
        'users/me/settings/publisher/',
        UpdatePublisherSettingsEndpoint.as_view(),
        name='update-publisher-settings'
    )
]