from elabodeal.web.views import BaseView


class UserSettingsView(BaseView):
    auth_required = True

    def get(self, request):
        return self.respond('user-settings.html', request)