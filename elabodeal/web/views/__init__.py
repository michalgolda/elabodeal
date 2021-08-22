from .base import BaseView, BaseAjaxView

from .cart import (
    CartView,
    CartCheckoutView
)
from .saved_carts import (
    SavedCartsView,
    SavedCartDetailsView
)
from .salesmanager import (
    SalesManagerIndexView, 
    SalesManagerStartView,
    SalesManagerAddProductView
)
from .index import IndexView
from .logout import LogoutView
from .product import ProductView
from .profile import ProfileView
from .settings import SettingsView
from .shared_cart import SharedCartView
from .auth import LoginView, RegisterView
from .reset_password import ResetPasswordView
from .search_results import SearchResultsView
from .purchased_products import PurchasedProductsView
from .user_register_confirmation import UserRegisterConfirmationView