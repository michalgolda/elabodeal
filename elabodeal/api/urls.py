from django.urls import path, include
from elabodeal.api.views.webhook import WebHookAPIView
from elabodeal.api.views.payment import PaymentAPIView

app_name = 'api'

urlpatterns = [
	path('webhooks/', WebHookAPIView.as_view(), name='webhooks'),
	path('payments/', PaymentAPIView.as_view(), name='payments')
]