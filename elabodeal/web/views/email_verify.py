from django.utils import timezone
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

from elabodeal.models import VerifyCode, User
from elabodeal.web.forms.email_verify import EmailVerifyForm


class EmailVerifyView(View):
	def get_form(self, request = None):
		return EmailVerifyForm(request.POST if request else None)

	def respond_verify_page(self, request, context = None):
		return HttpResponse(render_to_string('email_verify.html', context, request))

	def get(self, request):
		if not 'email' in request.session:
			return redirect('web:index')

		context = {
			'form': self.get_form(),
			'email': request.session['email']
		}
		return self.respond_verify_page(request, context)

	def post(self, request):
		form = self.get_form(request)
		if form.is_valid():
			verify_code = VerifyCode.objects.filter(email=request.session['email']).first()

			if verify_code.code == form.cleaned_data['code']:
				verify_code.delete()

				user = User.objects.filter(email=request.session['email']).first()
				user.email_verified = True
				user.email_verified_at = timezone.now()
				user.save()

				del request.session['email']

				return redirect('web:login')

			form.add_error('code', 'Niepoprawny kod weryfikacyjny. Spróbuj ponownie')

			context = {
				'form': form
			}
			return self.respond_verify_page(request, context)



		context = {
			'form': form
		}
		return self.respond_verify_page(request, context)