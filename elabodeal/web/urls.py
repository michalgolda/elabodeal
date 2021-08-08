from django.urls import include, path
from elabodeal.web.views import (
   	CartView,
    IndexView, 
    LoginView,
	LogoutView, 
	ProductView,
	RegisterView, 
	SettingsView,
	SharedCartView,
	SavedCartsView,
    CartCheckoutView,
	SearchResultsView,
	SavedCartDetailsView,
	SalesManagerStartView,
	SalesManagerIndexView, 
	PurchasedProductsView,
    EmailVerificationView, 
	SalesManagerAddProductView,
)

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('p/<uuid:id>/', ProductView.as_view(), name='product'),
	path('zaloguj/', LoginView.as_view(), name='login'),
	path('zarejestruj/', RegisterView.as_view(), name='register'),
	path('weryfikacja/', EmailVerificationView.as_view(), name='email-verification'),
	path('wyloguj/', LogoutView.as_view(), name='logout'),
	path('s/', SearchResultsView.as_view(), name='search-results'),
	path('purchased_products/', PurchasedProductsView.as_view(), name='purchased-products'),
	path('settings/', SettingsView.as_view(), name='settings'),
	path('c/', include([
		path('', CartView.as_view(), name='cart'),
		path('checkout/', CartCheckoutView.as_view(), name='cart-checkout')
	])),
	path('carts/', SavedCartsView.as_view(), name='saved-carts'),
	path('carts/<uuid:id>/', SavedCartDetailsView.as_view(), name='saved-cart-details'),
	path('m/', SalesManagerIndexView.as_view(), name='salesmanager'),
	path('m/start/', SalesManagerStartView.as_view(), name='salesmanager-start'),
	path('m/add_product/', SalesManagerAddProductView.as_view(), name='salesmanager-add-product'),
	path('shared_cart/<str:code>/', SharedCartView.as_view(), name='shared-cart')
]
