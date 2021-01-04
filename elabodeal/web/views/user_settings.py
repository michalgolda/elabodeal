import json

from elabodeal.models import User
from elabodeal.web.views import BaseView, BaseAjaxView


class UserSettingsView(BaseView):
    auth_required = True

    def get(self, request):
        user = request.user

        context = {'user': user}

        return self.respond('user-settings.html', request, context)


class UserUpdateSettingsAjaxView(BaseAjaxView):
    auth_required = True

    def post(self, request):
        user = request.user
        data = request.POST

        User.objects.update_settings(user, data)

        return self.respond(status=201)