from django.urls import path, include

from elabodeal.api.views.webhook import WebHookAPIView
from elabodeal.api.views.payment import PaymentAPIView
from elabodeal.api.views.files import FilesAPIView
from elabodeal.api.views.share import ShareCartAPIView
from elabodeal.api.views.product import ProductUpdateAPIView

app_name = 'api'

urlpatterns = [
	path('webhooks/', WebHookAPIView.as_view(), name='webhooks'),
	path('payments/', PaymentAPIView.as_view(), name='payments'),
	path('files/<str:name>/', FilesAPIView.as_view(), name='files'),
	path('share/carts/', ShareCartAPIView.as_view(), name='share-carts'),
	path('product/<int:id>/', ProductUpdateAPIView.as_view(), name='product-update')
]