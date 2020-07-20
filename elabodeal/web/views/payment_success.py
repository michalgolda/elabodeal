from django.shortcuts import redirect
from elabodeal.web.views.base import BaseView


class PaymentSuccessView(BaseView):
	def get(self, request):
		if 'payment' not in request.session:
			return redirect('web:index')

		email = request.session['payment']['email']
		
		del request.session['payment']
		del request.session['cart']

		context = {
			'email': email
		}
		return self.respond('payment_success.html', request, context)