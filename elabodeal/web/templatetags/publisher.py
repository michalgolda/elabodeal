import json

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(takes_context=True)
def get_publisher_context(context):
	user = context.request.user

	publisher_context = {}

	if user.is_authenticated and user.is_publisher:
		publisher = user.publisher

		publisher_context['id'] = str(publisher.id)
		publisher_context['swift'] = publisher.swift
		publisher_context['last_name'] = publisher.last_name
		publisher_context['first_name'] = publisher.first_name
		publisher_context['account_number'] = publisher.account_number

	return mark_safe(json.dumps(publisher_context))