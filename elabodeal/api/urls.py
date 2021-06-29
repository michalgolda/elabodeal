from django.urls import path, include

from elabodeal.api.endpoints import (
    MeProductsEndpoint,
    MeChangePasswordEndpoint,
    MeProductsGroupsEndpoint,
    MeUpdateSettingsEndpoint,
    MeProductsDetailsEndpoint,
    MeChangeEmailRequestEndpoint,
    MeProductsGroupsDetailsEndpoint,
    MeUpdatePublisherSettingsEndpoint,
    MeConfirmEmailChangeRequestEndpoint
)

app_name = 'api'

urlpatterns = [
    path(
        'me/',
        include([
            path(
                'products/',
                MeProductsEndpoint.as_view(),
                name='me-products'
            ),
            path(
                'products/<uuid:product_id>/',
                MeProductsDetailsEndpoint.as_view(),
                name='me-product-details'
            ),
            path(
                'products/groups/',
                MeProductsGroupsEndpoint.as_view(),
                name='me-products-groups'
            ),
            path(
                'products/groups/<uuid:product_group_id>/',
                MeProductsGroupsDetailsEndpoint.as_view(),
                name='me-product-group-details'
            ),
            path(
                'settings/',
                MeUpdateSettingsEndpoint.as_view(),
                name='me-update-settings'
            ),
            path(
                'settings/email/',
                MeChangeEmailRequestEndpoint.as_view(),
                name='me-change-email-request'
            ),
            path(
                'settings/email/confirm/',
                MeConfirmEmailChangeRequestEndpoint.as_view(),
                name='me-confirm-email-change-request'
            ),
            path(
                'settings/password/',
                MeChangePasswordEndpoint.as_view(),
                name='me-change-password'
            ),
            path(
                'settings/publisher/',
                MeUpdatePublisherSettingsEndpoint.as_view(),
                name='me-publisher-update-settings'
            )
        ])
    )
]