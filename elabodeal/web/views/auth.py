from django.shortcuts import redirect, reverse

from elabodeal.web.views import BaseView
from elabodeal.web.forms import LoginForm, RegisterForm


class LoginView(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('web:index')

        context = {'form': LoginForm()}

        return self.respond('login.html', request, context)

    def post(self, request):
        form = LoginForm(request)

        if form.is_valid(): 
            form.execute()

            return redirect('web:index')

        context = {'form': form}

        return self.respond('login.html', request, context)


class RegisterView(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('web:index') 

        context = {'form': RegisterForm()}

        return self.respond('register.html', request, context)

    def post(self, request):
        form = RegisterForm(request)

        if form.is_valid(): 
            form.execute()

            email = form.cleaned_data['email']

            register_confirmation_url = '{}.?email={}'.format(
                reverse('web:user-register-confirmation'),
                email
            )

            return redirect(register_confirmation_url)

        context = {'form': form}

        return self.respond('register.html', request, context)