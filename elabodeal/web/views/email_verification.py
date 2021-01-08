from django.shortcuts import redirect

from elabodeal.web.views import BaseView, BaseAjaxView
from elabodeal.models import VerificationCode, User
from elabodeal.web.forms import EmailVerificationForm


class EmailVerificationView(BaseView):
	def get_form(self, request = None):
		return EmailVerificationForm(request.POST if request else request)

	def get(self, request):
		session = request.session

		email_for_confirmation = session.get('email_for_confirmation')
		if not email_for_confirmation:
			return redirect('web:index')

		context = {
			'form': self.get_form(),
			'email': email_for_confirmation}

		return self.respond('email_verification.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		session = request.session

		if form.is_valid():
			code = form.cleaned_data.get('email')
			email = session.get('email_for_confirmation')

			if not VerificationCode.objects.verify(code, email):
				form.add_error(
					'code',
					'Coś poszło nie tak. Spróbuj ponownie.')

				context = {'form': form}

				return self.respond('email_verification.html', request, context)

			return redirect('web:index')


class EmailVerificationAjaxView(BaseAjaxView):
	def post(self, request):
		data = request.POST

		code = data.get('code')
		email = data.get('email')

		if not code or not email:
			return self.respond(message='BadRequest',
								status=400)

		try:
			VerificationCode.objects.verify(email, code)
		except ValueError as e:
			return self.respond(message=str(e),
								status=400)
		
		return self.respond(message='Success verified email address')


class ResendEmailVerificationAjaxView(BaseAjaxView):
	def post(self, request):
		data = request.POST

		email = data.get('email')

		if not email:
			return self.respond(message='BadRequest',
								status=400)

		try:
			VerificationCode.objects.generate(email)
		except ValueError as e:
			return self.respond(message=str(e),
								status=400)

		return self.respond(message='Success generated new verification code')
		


