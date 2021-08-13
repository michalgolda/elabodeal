from elabodeal.web.views import BaseView


class SettingsView(BaseView):
	auth_required = True

	def get(self, request):
		user = request.user
		
		user_context = {
			'id': str(user.id),
			'email': user.email,
			'username': user.username,
			'newsletter': user.newsletter,
			'is_publisher': user.is_publisher,
			'email_verified': user.email_verified
		}

		publisher = user.publisher if user.is_publisher else None

		publisher_context = {
			'id': str(publisher.id),
			'swift': publisher.swift,
			'last_name': publisher.last_name,
			'first_name': publisher.first_name,
			'account_number': publisher.account_number
		} if publisher else {}

		context = {
			'application_data': {
				'user': user_context,
				'publisher': publisher_context
			}
		}

		return self.respond('settings.html', request, context)