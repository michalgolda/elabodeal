from elabodeal.web.views.base import BaseView

from elabodeal.web.forms.delivery import DeliveryForm

class DeliveryView(BaseView):
	def get_form(self, request = None):
		return DeliveryForm(request.POST if request else None)

	def get(self, request):

		context = {
			'form': self.get_form()
		}
		return self.respond('delivery.html', request, context)