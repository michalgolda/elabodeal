from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def get_stripe_public_api_key() -> str:
	api_key = settings.STRIPE_PUBLIC_API_KEY
	return api_key