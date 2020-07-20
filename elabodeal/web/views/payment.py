from django.shortcuts import redirect
from elabodeal.web.views.base import BaseView


class PaymentView(BaseView):
	def get(self, request):
		if not 'payment' in request.session:
			return redirect('web:index')
			
		return self.respond('payment.html', request)