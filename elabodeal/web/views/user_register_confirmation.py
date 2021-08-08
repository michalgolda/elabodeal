from elabodeal.web.views import BaseView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from elabodeal.models import User


def check_user_ready_to_confirmation(method):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('web:index')

        email = request.GET.get('email')

        if not email: 
            return redirect('web:index')

        existing_user = User.objects.filter(email=email).first()

        if not existing_user: 
            return redirect('web:index')

        ready_to_confirmation = not existing_user.email_verified

        if not ready_to_confirmation: 
            return redirect('web:index')

        return method(request, *args, **kwargs)
    return wrapper


class UserRegisterConfirmationView(BaseView):

    @method_decorator(check_user_ready_to_confirmation)
    def get(self, request):
        return self.respond('user-register-confirmation.html', request)