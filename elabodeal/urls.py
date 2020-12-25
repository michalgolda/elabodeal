from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('elabodeal.web.urls')),
	path('admin/', admin.site.urls)
]