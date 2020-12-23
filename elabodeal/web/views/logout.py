from django.contrib.auth import logout
from django.shortcuts import redirect

from elabodeal.web.views import BaseView


class LogoutView(BaseView):
	def get(self, request):
		user = request.user
		user.is_online = False
		user.save()

		logout(request)

		return redirect('web:index')