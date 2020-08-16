from django.urls import path, include

from elabodeal.web.views.auth import LoginView, RegisterView
from elabodeal.web.views.index import IndexView
from elabodeal.web.views.email_verify import EmailVerifyView
from elabodeal.web.views.product_detail import ProductDetailView
from elabodeal.web.views.logout import LogoutView
from elabodeal.web.views.cart import CartView
from elabodeal.web.views.saved_carts import SavedCartsView
from elabodeal.web.views.saved_cart_detail import SavedCartDetailView
from elabodeal.web.views.salesmanager import SalesManagerView
from elabodeal.web.views.salesmanager_start import SalesManagerStartView
from elabodeal.web.views.salesmanager_add_product import SalesManagerAddProductView
from elabodeal.web.views.delivery import DeliveryView
from elabodeal.web.views.payment import PaymentView
from elabodeal.web.views.payment_success import PaymentSuccessView
from elabodeal.web.views.my_books import MyBooksView
from elabodeal.web.views.purchased_product_detail import PurchasedProductDetailView
from elabodeal.web.views.shared_cart import SharedCartView

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('product/<str:url_name>/', ProductDetailView.as_view(), name='product-detail'),
	path('auth/login/', LoginView.as_view(), name='login'),
	path('auth/register/', RegisterView.as_view(), name='register'),
	path('account/verify/', EmailVerifyView.as_view(), name='account-email-verify'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('mybooks/', MyBooksView.as_view(), name='my-books'),
	path('mybooks/<int:id>/', PurchasedProductDetailView.as_view(), name='purchased-product-detail'),
	path('cart/', include([
		path('', CartView.as_view(), name='cart'),
		path('delivery/', DeliveryView.as_view(), name='cart-delivery'),
		path('payment/', PaymentView.as_view(), name='cart-payment')
	])),
	path('success/', PaymentSuccessView.as_view(), name='payment-success'),
	path('saved/carts/', SavedCartsView.as_view(), name='saved-carts'),
	path('saved/carts/<int:id>/', SavedCartDetailView.as_view(), name='saved-cart-detail'),
	path('salesmanager/', include([
		path('', SalesManagerView.as_view(), name='salesmanager'),
		path('addproduct/', SalesManagerAddProductView.as_view(), name='salesmanager-add-product'),
		path('start/', SalesManagerStartView.as_view(), name='salesmanager-start')
	])),
	path('shared/carts/<str:code>/', SharedCartView.as_view(), name='shared-cart')
]