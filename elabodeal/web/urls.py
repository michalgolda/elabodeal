from django.urls import path

from elabodeal.web.views.auth import LoginView, RegisterView
from elabodeal.web.views.index import IndexView
from elabodeal.web.views.email_verify import EmailVerifyView

app_name = 'web'

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('auth/login/', LoginView.as_view(), name='login'),
	path('auth/register/', RegisterView.as_view(), name='register'),
	path('account/verify/', EmailVerifyView.as_view(), name='account-email-verify')
]