from django.urls import path, include

from elabodeal.api.endpoints import (
    # ConfirmEmailEndpoint,
    # ResendConfirmEmailEndpoint,
    # ResendConfirmChangeEmailEndpoint,
    # UpdateUserSettingsEndpoint,
    # UpdatePublisherSettingsEndpoint,
    # SaveCartEndpoint,
    # ShareCartEndpoint,
    MeProductsGroupsEndpoint,
    MeProductsGroupsDetailsEndpoint
)

app_name = 'api'

urlpatterns = [
    # path(
    #     'verify/email/',
    #     ConfirmEmailEndpoint.as_view(),
    #     name='confirm-email-verification-code'
    # ),
    # path(
    #     'verify/email/resend/',
    #     ResendConfirmEmailEndpoint.as_view(),
    #     name='resend-email-verification-code'
    # ),
    # path(
    #     'verify/email/change/resend/',
    #     ResendConfirmChangeEmailEndpoint.as_view(),
    #     name='resend-change-email-confirmation'
    # ),
    # path(
    #     'users/me/settings/',
    #     UpdateUserSettingsEndpoint.as_view(),
    #     name='update-user-settings'
    # ),
    # path(
    #     'users/me/settings/publisher/',
    #     UpdatePublisherSettingsEndpoint.as_view(),
    #     name='update-publisher-settings'
    # ),
    # path(
    #     'users/me/carts/',
    #     SaveCartEndpoint.as_view(),
    #     name='save-cart'
    # ),
    # path(
    #     'users/me/carts/<int:id>/share/',
    #     ShareCartEndpoint.as_view(),
    #     name='share-cart'
    # ),
    path(
        'me/',
        include([
            # path(
            #     'products/',
            #     MeProductsEndpoint.as_view(),
            #     name='me-products'
            # ),
            # path(
            #     'products/<int:product_id>/',
            #     MeProductDetailsEndpoint.as_view(),
            #     name='me-product-details'
            # ),
            path(
                'products/groups/',
                MeProductsGroupsEndpoint.as_view(),
                name='me-products-groups'
            ),
            path(
                'products/groups/<uuid:product_group_id>/',
                MeProductsGroupsDetailsEndpoint.as_view(),
                name='me-product-group-details'
            )
        ])
    )
]