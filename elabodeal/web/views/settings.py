from elabodeal.web.views import BaseView


class SettingsView(BaseView):
	auth_required = True

	def get(self, request):
		return self.respond('settings.html', request)