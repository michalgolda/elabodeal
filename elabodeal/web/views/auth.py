import random

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.template.loader import render_to_string

from elabodeal.web.views.base import BaseView
from elabodeal.models import VerifyCode
from elabodeal.web.forms.auth import LoginForm, RegisterForm


class LoginView(BaseView):
	def get_form(self, request = None):
		return LoginForm(request.POST if request else None)

	def get(self, request):
		form = self.get_form()
		context = {
			'form': form
		}
		return self.respond('auth/login.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))

			if user is not None:
				if user.email_verified:
					login(request, user)

					return redirect('web:index')

				form.add_error('email', 'Za nim się zalogujesz musisz zweryfikować konto')
				context = {
					'form': form
				}
				return self.respond('auth/login.html', request, context)

			form.add_error('email', 'Nieprawidłowy email lub hasło')
			context = {
				'form': form
			}
			return self.respond('auth/login.html', request, context)


		context = {
			'form': form
		}
		return self.respond('auth/login.html', request, context)


class RegisterView(BaseView):
	def get_form(self, request = None):
		return RegisterForm(request.POST if request else None)

	def get(self, request):
		form = self.get_form()
		context = {
			'form': form
		}
		return self.respond('auth/register.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():

			code = ''.join(str(random.randint(0, 9)) for _ in range(6))

			try:
				send_mail(
					subject='Elabodeal - Weryfikacja konta',
					message=f'To jest twój kod weryfikacyjny {code}',
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=[form.cleaned_data['email']],
					html_message=render_to_string('emails/verification.html', {'code': code})
				)
			except:
				return redirect('web:register')

			verify_codes = VerifyCode.objects.filter(email=form.cleaned_data['email']).all()
			verify_codes.delete()

			verify_code = VerifyCode(
				email=form.cleaned_data['email'],
				code=code
			)

			form.save()
			verify_code.save()

			request.session['email'] = form.cleaned_data['email'];

			return redirect('web:account-email-verify')

		context = {
			'form': form
		}
		return self.respond('auth/register.html', request, context)