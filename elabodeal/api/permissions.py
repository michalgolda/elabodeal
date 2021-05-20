from rest_framework.permissions import BasePermission


class PublisherOnlyAccess(BasePermission):
	message = 'You are not publisher.'

	def has_permission(self, request, view):
		user = request.user

		if user.is_anonymous: return False

		return user.is_publisher