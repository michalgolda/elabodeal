import json

from elabodeal.models import User, VerificationCode
from elabodeal.web.views import BaseView, BaseAjaxView


class UserSettingsView(BaseView):
    auth_required = True

    def get(self, request):
        return self.respond('user-settings.html', request, context)