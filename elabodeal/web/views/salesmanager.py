from elabodeal.web.views.base import BaseView


class SalesManagerView(BaseView):
	auth_required = True
	seller_required = True

	def get(self, request):
		return self.respond('salesmanager/index.html', request)