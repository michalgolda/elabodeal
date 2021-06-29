import json

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(takes_context=True)
def get_user_context(context):
	user = context.request.user

	user_context = {}

	if user.is_authenticated:
		user_context['id'] = str(user.id)
		user_context['email'] = user.email
		user_context['username'] = user.username
		user_context['email_verified'] = user.email_verified
		user_context['newsletter'] = user.newsletter 

		user_context['isAuthenticated'] = True
		user_context['isPublisher'] = user.is_publisher

	return mark_safe(json.dumps(user_context))