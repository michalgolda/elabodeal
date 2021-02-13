from django.shortcuts import redirect

from elabodeal.web.views import BaseView
from elabodeal.models import User


class EmailVerificationView(BaseView):
	def get(self, request):
		email_for_confirmation = request.session.get('email_for_confirmation')
		if not email_for_confirmation:
			return redirect('web:index')

		existing_user = User.objects.filter(email=email_for_confirmation).first()
		if not existing_user:
			return redirect('web:index')

		if existing_user.email_verified:
			return redirect('web:index')

		context = {
			'email': email_for_confirmation
		}

		return self.respond('email_verification.html', request, context)