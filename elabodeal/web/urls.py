from django.urls import include, path
from elabodeal.web.views import (
   	CartView,
    IndexView, 
    LoginView,
	LogoutView, 
	ProfileView,
	ProductView,
	RegisterView, 
	SettingsView,
	SharedCartView,
	SavedCartsView,
    CartCheckoutView,
	ResetPasswordView,
	SearchResultsView,
	SavedCartDetailsView,
	SalesManagerStartView,
	SalesManagerIndexView, 
	PurchasedProductsView,
	SalesManagerAddProductView,
    UserRegisterConfirmationView
)

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', RegisterView.as_view(), name='register'),
	path('cart/', CartView.as_view(), name='cart'),
	path('cart/checkout/', CartCheckoutView.as_view(), name='cart-checkout'),
	path('carts/', SavedCartsView.as_view(), name='saved-carts'),
	path('carts/<uuid:id>/', SavedCartDetailsView.as_view(), name='saved-cart-details'),
	path('m/', SalesManagerIndexView.as_view(), name='salesmanager'),
	path('m/start/', SalesManagerStartView.as_view(), name='salesmanager-start'),
	path('m/add_product/', SalesManagerAddProductView.as_view(), name='salesmanager-add-product'),
	path('settings/', SettingsView.as_view(), name='settings'),
	path('product/<uuid:id>/', ProductView.as_view(), name='product'),
	path('profiles/<str:username>/', ProfileView.as_view(), name='profiles'),
	path('results/', SearchResultsView.as_view(), name='search-results'),
	path('shared_cart/<str:code>/', SharedCartView.as_view(), name='shared-cart'),
	path('purchased_products/', PurchasedProductsView.as_view(), name='purchased-products'),
	path('confirm/', UserRegisterConfirmationView.as_view(), name='user-register-confirmation'),
	path('reset-password/', ResetPasswordView.as_view(), name='reset-password')
]
