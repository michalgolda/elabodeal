from django.urls import path
from elabodeal.api.views.hello import HelloAPIView

urlpatterns = [
	path('', HelloAPIView.as_view())
]