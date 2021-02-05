from django.urls import path

from elabodeal.api.endpoints import (
    ConfirmEmailEndpoint,
    ResendConfirmEmailEndpoint,
    UpdateUserSettingsEndpoint,
    UpdatePublisherSettingsEndpoint,
    SaveCartEndpoint
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
    ),
    path(
        'users/me/carts/',
        SaveCartEndpoint.as_view(),
        name='save-cart'
    )
]