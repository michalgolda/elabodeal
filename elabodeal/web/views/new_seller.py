from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.web.forms.new_seller import NewSellerForm


class NewSellerView(BaseView):
	auth_required = True

	def get_form(self, request = None):
		return NewSellerForm(request.POST if request else None)

	def get(self, request):
		context = {
			'form': self.get_form()
		}
		return self.respond('new_seller.html', request, context)