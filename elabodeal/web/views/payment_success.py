from django.shortcuts import redirect
from elabodeal.web.views.base import BaseView


class PaymentSuccessView(BaseView):
	def get(self, request):
		if 'delivery' not in request.session:
			return redirect('web:index')

		email = request.session['delivery']['email']
		
		del request.session['delivery']
		del request.session['cart']

		context = {
			'email': email
		}
		return self.respond('payment_success.html', request, context)