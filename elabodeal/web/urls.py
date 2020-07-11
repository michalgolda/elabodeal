from django.urls import path, include

from elabodeal.web.views.auth import LoginView, RegisterView
from elabodeal.web.views.index import IndexView
from elabodeal.web.views.email_verify import EmailVerifyView
from elabodeal.web.views.product_detail import ProductDetailView
from elabodeal.web.views.logout import LogoutView
from elabodeal.web.views.cart import CartView
from elabodeal.web.views.salesmanager import SalesManagerView
from elabodeal.web.views.salesmanager_start import SalesManagerStartView
from elabodeal.web.views.salesmanager_add_product import SalesManagerAddProductView

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('product/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
	path('auth/login/', LoginView.as_view(), name='login'),
	path('auth/register/', RegisterView.as_view(), name='register'),
	path('account/verify/', EmailVerifyView.as_view(), name='account-email-verify'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('cart/', CartView.as_view(), name='cart'),
	path('salesmanager/', include([
		path('', SalesManagerView.as_view(), name='salesmanager'),
		path('addproduct/', SalesManagerAddProductView.as_view(), name='salesmanager-add-product'),
		path('start/', SalesManagerStartView.as_view(), name='salesmanager-start')
	]))
]