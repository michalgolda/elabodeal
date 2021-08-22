from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from elabodeal.web.views import BaseView


def only_unauthenticated_users(method):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated: 
            return redirect('web:index')
        
        return method(request, *args, **kwargs)
    return wrapper


class ResetPasswordView(BaseView):
    
    @method_decorator(only_unauthenticated_users)
    def get(self, request):
        return self.respond('reset_password.html', request)