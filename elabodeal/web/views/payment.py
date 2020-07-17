from elabodeal.web.views.base import BaseView


class PaymentView(BaseView):
	def get(self, request):
		return self.respond('payment.html', request)