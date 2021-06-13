from .base import BaseView, BaseAjaxView

from .cart import (
    CartView, 
    CartAddItemAction,
    CartDeleteItemAction,
    CartCheckoutDeliveryView, 
    CartCheckoutPaymentView,
    CartCheckoutPaymentAjaxView, 
    CartCheckoutPaymentSuccessView
)
from .salesmanager import (
    SalesManagerIndexView, 
    SalesManagerStartView,
    SalesManagerAddProductView
)
from .index import IndexView
from .logout import LogoutView
from .settings import SettingsView
from .shared_cart import SharedCartView
from .auth import LoginView, RegisterView
from .product_detail import ProductDetailView
from .search_results import SearchResultsView
from .email_verification import EmailVerificationView
from .purchased_products import PurchasedProductsView