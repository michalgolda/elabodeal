from .base import BaseView, BaseAjaxView
from .index import IndexView
from .logout import LogoutView
from .auth import LoginView, RegisterView
from .salesmanager import (SalesManagerIndexView, 
                           SalesManagerStartView,
                           SalesManagerAddProductView)
from .product_detail import ProductDetailView
from .search_results import SearchResultsView
from .cart import (CartView, CartAddItemAction,
                   CartDeleteItemAction, CartSaveAjaxView,
                   CartCheckoutDeliveryView, CartCheckoutPaymentView,
                   CartCheckoutPaymentAjaxView, CartCheckoutPaymentSuccessView)
from .email_verification import (EmailVerificationView, EmailVerificationAjaxView,
                                 ResendEmailVerificationAjaxView)
from .saved_carts import SavedCartsView, SavedCartShareAjaxView
from .saved_cart_detail import SavedCartDetailView
from .purchased_products import PurchasedProductsView
from .shared_cart import SharedCartView
from .user_settings import UserSettingsView, UserSaveSettingsAjaxView