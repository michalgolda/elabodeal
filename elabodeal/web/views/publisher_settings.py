from elabodeal.web.views import BaseView


class PublisherSettingsView(BaseView):
    auth_required = True

    def get(self, request):
        return self.respond('publisher-settings.html', request)