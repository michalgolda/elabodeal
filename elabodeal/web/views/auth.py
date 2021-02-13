from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from elabodeal.web.views import BaseView
from elabodeal.web.forms import LoginForm, RegisterForm


class LoginView(BaseView):
	def get_form(self, request = None):
		return LoginForm(request.POST if request else request)

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('web:index')

		form = self.get_form()

		context = {'form': form}

		return self.respond('auth/login.html', 
							request, 
							context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			email = request.POST.get('email')
			password = request.POST.get('password')

			user = authenticate(request, 
								email=email, 
								password=password)

			if user is not None:
				login(request, user)

				user.is_online = True
				user.save()

				return redirect('web:index')

			form.add_error('email', 
						   'Nieprawidłowy email lub hasło')
			
			context = {'form': form}
		
			return self.respond('auth/login.html', 
								request, 
								context)

		context = {'form': form}

		return self.respond('auth/login.html', 
							request, 
							context)


class RegisterView(BaseView):
	def get_form(self, request = None):
		return RegisterForm(request.POST if request else request)

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('web:index')

		form = self.get_form()
		
		context = {'form': form}

		return self.respond('auth/register.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			email_for_confirmation = form.cleaned_data.get('email')

			form.save()

			request.session['email_for_confirmation'] = email_for_confirmation

			return redirect('web:email-verification')

		context = {'form': form}

		return self.respond('auth/register.html', request, context)