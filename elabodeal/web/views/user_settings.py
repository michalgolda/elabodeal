import json

from elabodeal.models import User, VerificationCode
from elabodeal.web.views import BaseView, BaseAjaxView


class UserSettingsView(BaseView):
    auth_required = True

    def get(self, request):
        user = request.user

        if not user.email_verified:
            email = user.email
            
            VerificationCode.objects.generate(email)

        context = {'user': user}

        return self.respond('user-settings.html', request, context)


class UserSaveSettingsAjaxView(BaseAjaxView):
    auth_required = True

    def post(self, request):
        user = request.user
        data = request.POST

        User.objects.update_settings(user, data)

        return self.respond(message='Success',
                            status=200)