from django.shortcuts import redirect

from elabodeal.web.views import BaseView
from elabodeal.web.forms import StartSellingForm


class SalesManagerStartView(BaseView):
	auth_required = True

	def get_form(self, request = None):
		return StartSellingForm(request.POST if request else request)

	def get(self, request):
		user = request.user

		if user.publisher:
			return redirect('web:salesmanager')

		context = {'form': self.get_form()}

		return self.respond('salesmanager/start.html', 
							request, context)

	def post(self, request):
		form = self.get_form(request)

		if not form.is_valid():
			context = {'form': form}

			return redirect('web:salesmanager-start')

		user = request.user

		form.save(user)

		return redirect('web:index')

		