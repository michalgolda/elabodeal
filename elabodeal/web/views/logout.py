from django.contrib.auth import logout
from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView

class LogoutView(BaseView):
	def get(self, request):
		logout(request)

		return redirect('web:index')