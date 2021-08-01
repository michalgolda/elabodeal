from django.shortcuts import redirect

from elabodeal.web.views import BaseView


class SalesManagerStartView(BaseView):
	auth_required = True

	def get(self, request):
		SUPPORTED_COUNTRIES = ['Polska', 'Niemcy']

		context = {
			'application_data': {
				'supported_countries': SUPPORTED_COUNTRIES
			}
		}

		return self.respond('salesmanager/start.html', request, context)