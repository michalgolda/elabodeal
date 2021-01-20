from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('elabodeal.web.urls')),
	path('api/', include('elabodeal.api.urls')),
	path('admin/', admin.site.urls)
]