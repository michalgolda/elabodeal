from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def stripe_publishable_key():
	return settings.STRIPE_PUBLISHABLE_KEY