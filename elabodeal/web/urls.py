from django.urls import include, path
from elabodeal.web.views import (CartAddItemAction, CartCheckoutDeliveryView,
                                 CartCheckoutPaymentAjaxView,
                                 CartCheckoutPaymentSuccessView,
                                 CartCheckoutPaymentView, CartDeleteItemAction,
                                 CartSaveAjaxView, CartView,
                                 EmailVerificationView, IndexView, LoginView,
                                 LogoutView, ProductDetailView,
                                 PurchasedProductsView, RegisterView,
                                 SalesManagerAddProductView,
                                 SalesManagerIndexView, SalesManagerStartView,
                                 SavedCartDetailView, SavedCartShareAjaxView,
                                 SavedCartsView, SearchResultsView,
                                 SharedCartView, UserSettingsView,
								 UserSaveSettingsAjaxView, EmailVerificationAjaxView,
								 ResendEmailVerificationAjaxView)

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('p/<str:url_name>/', ProductDetailView.as_view(), name='product-detail'),
	path('zaloguj/', LoginView.as_view(), name='login'),
	path('zarejestruj/', RegisterView.as_view(), name='register'),
	path('weryfikacja/', EmailVerificationView.as_view(), name='email-verification'),
	path('verify/ajax/email/', EmailVerificationAjaxView.as_view(), name='verify-email'),
	path('verify/ajax/email/resend/', ResendEmailVerificationAjaxView.as_view(), name='resend-email-verification-code'),
	path('wyloguj/', LogoutView.as_view(), name='logout'),
	path('s/', SearchResultsView.as_view(), name='search-results'),
	path('mp/', PurchasedProductsView.as_view(), name='purchased-products'),
	path('settings/', UserSettingsView.as_view(), name='user-settings'),
	path('settings/ajax/save/', UserSaveSettingsAjaxView.as_view(), name='user-settings-save'),
	path('c/', include([
		path('', CartView.as_view(), name='cart'),
		path('ajax/', include([
			path('add-item/', CartAddItemAction.as_view(), name='cart-action-add-item'),
			path('delete-item/', CartDeleteItemAction.as_view(), name='cart-action-delete-item'),
			path('save/', CartSaveAjaxView.as_view(), name='cart-action-save'),
		])),
		path('checkout/', include([
			path('d/', CartCheckoutDeliveryView.as_view(), name='cart-checkout-delivery'),
			path('p/', include([
				path('', CartCheckoutPaymentView.as_view(), name='cart-checkout-payment'),
				path('ajax/', include([
					path('payment_init/', CartCheckoutPaymentAjaxView.as_view(), name='cart-checkout-payment-init')
				])),
				path('success/', CartCheckoutPaymentSuccessView.as_view(), name='cart-checkout-payment-success')
			])),
		])),
	])),
	path('sc/', include([
		path('', SavedCartsView.as_view(), name='saved-carts'),
		path('<int:id>/', SavedCartDetailView.as_view(), name='saved-cart-detail'),
		path('ajax/', include([
			path('share/', SavedCartShareAjaxView.as_view(), name='saved-cart-share'),
		])),
	])),
	path('m/', include([
		path('', SalesManagerIndexView.as_view(), name='salesmanager'),
		path('p/', SalesManagerAddProductView.as_view(), name='salesmanager-add-product'),
		path('start/', SalesManagerStartView.as_view(), name='salesmanager-start'),
		# path('product/<int:id>/', SalesManagerPreviewProductView.as_view(), name='salesmanager-preview-product')
	])),
	path('shc/<str:code>/', SharedCartView.as_view(), name='shared-cart-detail')
]
