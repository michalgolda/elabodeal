from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.web.forms.delivery import DeliveryForm


class DeliveryView(BaseView):
	def get_form(self, request = None):
		return DeliveryForm(request.POST if request else None)

	def get(self, request):
		if not 'cart' in request.session:
			return redirect('web:cart')
		if request.session['cart']['item_count'] <= 0:
			return redirect('web:cart')

		context = {
			'form': self.get_form()
		}
		return self.respond('delivery.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			if form.cleaned_data['gift']:
				request.session['payment'] = {
					'ready': True,
					'gift': form.cleaned_data['gift'],
					'gift_email': form.cleaned_data['gift_email'],
					'gift_first_name': form.cleaned_data['gift_first_name'],
					'gift_last_name': form.cleaned_data['gift_last_name'],
					'email': form.cleaned_data['email'],
					'first_name': form.cleaned_data['first_name'],
					'last_name': form.cleaned_data['last_name']
				}
			else:
				request.session['payment'] = {
					'ready': True,
					'email': form.cleaned_data['email'],
					'first_name': form.cleaned_data['first_name'],
					'last_name': form.cleaned_data['last_name']
				}

			return redirect('web:cart-payment')

		context = {
			'form': form
		}
		return self.respond('delivery.html', request, context)